import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_all_quotes():
    try:
        # Fetch all entries from the quotes table
        response = supabase.table("quotes").select("content, author, source").execute()

        if not response.data:
            print("No quotes found.")
            return

        # Open a file to save quotes
        with open('quotes.txt', 'w') as f:
            for entry in response.data:
                content = entry['content'] or "No content provided"
                author = entry['author'] or "Unknown author"
                source = entry['source'] or "No source provided"
                
                # Write the quote with details to the file
                f.write(f"{content}\n")
                f.write(f"  - Author: {author}\n")
                f.write(f"  - Source: {source}\n\n")

        print("Quotes saved to 'quotes.txt'.")

    except Exception as e:
        print("SOMETHING FUCKED UP")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    get_all_quotes()
