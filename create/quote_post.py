import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def add_quote():
    # Get user input for the quote
    content = input("Enter the quote content: ")
    author = input("Enter the author's name: ")
    source = input("Enter the source (if any): ")
    


    if not source:
        source = None  
    

    # Prepare the data payload
    data = {
        'content': content,
        'author': author,
        'source': source
    }

    # Insert the quote into the Supabase table
    response = supabase.table("quotes").insert(data).execute()
    
    print("Quote added successfully.")




if __name__ == "__main__":
    add_quote()

