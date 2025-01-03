import re
import os
import sys
import random
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def parse_post(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract metadata from the template
    metadata = re.search(
        r"ID=\"(.*)\"\nTITLE=\"(.*)\"\nLINK=\"(.*)\"\nIS_DRAFT=(.*)\nIS_POPULAR=(.*)\nTAGS=\[(.*)\]\n-{10}\n", content, re.DOTALL
    )
    if not metadata:
        raise ValueError("Invalid file format or metadata missing")

    post_id, title, link, is_draft, is_popular, tags = metadata.groups()
    tags = tags.split(",") if tags else []

    # Extract content after the metadata
    post_content = content[metadata.end():].strip()

    # Extract notes from the content
    notes_match = re.search(r"---NOTES---(.*?)---END NOTES---", post_content, re.DOTALL)
    notes = notes_match.group(1).strip() if notes_match else None
    if notes:
        # Remove notes section from post content
        post_content = post_content[:notes_match.start()].strip() + post_content[notes_match.end():].strip()

    content_peek = post_content[:200] + \
        '...' if len(post_content) > 200 else post_content

    post_id = int(post_id) if post_id else None

    return {
        'id': post_id,
        'title': title,
        'post_link': link,
        'post_content': post_content,
        'content_peek': clean_post_peek(content_peek),
        'is_draft': is_draft.upper() == 'T',
        'is_popular': is_popular.upper() == 'T',
        'tags': tags,
        'notes': notes  # Include notes for reference
    }, content[:metadata.start()]


def clean_post_peek(content_peek):
    cleaned_peek = []
    skip_mode = False
    # skip mode 2 for < jank but idc
    skip_mode_2 = False

    for char in content_peek:
        if char == "#":
            continue  # Skip hashtags
        if char == "(":
            skip_mode = True  # Start skipping characters inside brackets
            continue
        if char == ")":
            skip_mode = False  # End skipping characters inside brackets
            continue

        if char == "]" or char == "[":
            continue;

        if char == "<":
            skip_mode_2 = True
            continue

        if char == ">":
            skip_mode_2 = False
            continue

        if not skip_mode and not skip_mode_2:
            cleaned_peek.append(char)

    return ''.join(cleaned_peek)


def update_file_with_id(file_path: str, post_id: int, third):
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        updated = False
        for i, line in enumerate(lines):
            # Check if the line contains the ID metadata
            if line.startswith('ID="'):
                # Replace the existing ID value with the new post_id
                lines[i] = f'ID="{post_id}"\n'
                updated = True
                break

        # If the ID was found and updated, rewrite the file
        if updated:
            file.seek(0)
            file.writelines(lines)
            file.truncate()

def upload_post_to_supabase(file_path: str, data):
    header = data.pop('header', None)
    notes = data.pop('notes', None)  # Exclude notes from database upload

    db_data = {
        key: data[key] for key in data if key != 'header'
    }

    if db_data.get('id'):
        print("Updating post with id " + str(db_data['id']))
        response = supabase.table("posts").update(
            db_data).eq('id', db_data['id']).execute()
        db_data['tags'] = db_data.get('tags', [])
    else:
        print("Inserting new post")
        new_post_id = random.randint(0, 1000000000000000)
        db_data['id'] = new_post_id
        db_data['tags'] = db_data.get('tags', [])
        response = supabase.table("posts").insert(db_data).execute()
        update_file_with_id(file_path, new_post_id, header)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" * 5)
        print("new id is" + str(db_data['id']))

    print(response)
    print("Post uploaded successfully.")
    if notes:
        print("Notes retained in the .md file:")
        print(notes)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_post_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        post_data, header = parse_post(file_path)
        post_data['header'] = header
        upload_post_to_supabase(file_path, post_data)
        print("-=-=-=-=-=-=-=-=--=-=")
        print("LINKS IS")
        print("https://joshshipton.com/post/" + post_data["post_link"])
    except Exception as e:
        print(f"Error: {e}")
