'''
Python Script to add or update post to the Supabase table let's me work on posts in NeoVim and organise everything in the command line.
'''
import re
import os
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
    metadata = re.search(r"TTITLE=\"(.*)\"\nLINK=\"(.*)\"\nID=\"(.*)\"\nIS_DRAFT=(.*)\nIS_POPULAR=(.*)\n-{10}\n", content, re.DOTALL)
    if not metadata:
        raise ValueError("Invalid file format or metadata missing")

    title, link, post_id, is_draft, is_popular = metadata.groups()
    post_content = content[metadata.end():].strip()  # Extract content after the metadata
    content_peek = post_content[:200] + '...' if len(post_content) > 200 else post_content

    return {
        'id': int(post_id) if post_id else None,
        'title': title,
        'post_link': link,
        'post_content': post_content,
        'content_peek': content_peek,
        'is_draft': is_draft.lower() == 'true',
        'is_popular': is_popular.lower() == 'true'
    }, content[:metadata.start()]

def update_file_with_id(file_path: str, post_id: int, header: str):
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        file.seek(0)
        file.write(header + f"ID=\"{post_id}\"\n" + content)
        file.truncate()

def upload_post_to_supabase(file_path: str, data):
    if data['id']:
        # Update existing post
        response = supabase.table("posts").update(data).eq('id', data['id']).execute()
    else:
        # Insert new post
        response = supabase.table("posts").insert(data).execute()

        if not response.get('error') and response.get('data'):
            new_id = response['data'][0]['id']
            update_file_with_id(file_path, new_id, data['header'])

    if response.get('error'):
        print(f"Error: {response['error']}")
    else:
        print("Post uploaded successfully.")

if __name__ == "__main__":
    file_path = input("Enter the path to the post file: ")
    try:
        post_data, header = parse_post(file_path)
        post_data['header'] = header  # Include header for updating the file
        upload_post_to_supabase(file_path, post_data)
    except Exception as e:
        print(f"Error: {e}")

