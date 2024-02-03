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
        r"ID=\"(.*)\"\nTITLE=\"(.*)\"\nLINK=\"(.*)\"\nIS_DRAFT=(.*)\nIS_POPULAR=(.*)\n-{10}\n", content, re.DOTALL)
    if not metadata:
        raise ValueError("Invalid file format or metadata missing")

    post_id, title, link, is_draft, is_popular = metadata.groups()
    # Extract content after the metadata
    post_content = content[metadata.end():].strip()
    content_peek = post_content[:200] + \
        '...' if len(post_content) > 200 else post_content

    post_id = int(post_id) if post_id else None

    print("title is" + title, "link is" + link, "post_id is" +
          str(post_id), "is_draft is" + is_draft, "is_popular is" + is_popular)

    return {
        'id': post_id,
        'title': title,
        'post_link': link,
        'post_content': post_content,
        'content_peek': content_peek,
        'is_draft': is_draft.upper() == 'T',
        'is_popular': is_popular.upper() == 'T'
    }, content[:metadata.start()]


def update_file_with_id(file_path: str, post_id: int):
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

    db_data = {
        key: data[key] for key in data if key != 'header'
    }

    print(db_data)

    if db_data.get('id'):
        print("Updating post with id " + str(db_data['id']))
        response = supabase.table("posts").update(
            db_data).eq('id', db_data['id']).execute()
    else:
        print("Inserting new post")
        new_post_id = random.randint(0, 100000)
        db_data['id'] = new_post_id
        response = supabase.table("posts").insert(db_data).execute()
        update_file_with_id(file_path, new_post_id, header)

    print(response)
    print("Post uploaded successfully.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_post_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        post_data, header = parse_post(file_path)
        post_data['header'] = header
        upload_post_to_supabase(file_path, post_data)
    except Exception as e:
        print(f"Error: {e}")
