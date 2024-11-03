import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_all_emails():
    try:
        # Get all entries from the subs table
        response = supabase.table("subs").select("email, name, date_added").execute()

        # Extract emails and join them with commas
        emails = [sub['email'] for sub in response.data]
        email_string = ", ".join(emails)

        print("\nEmail list:")
        print("-----------")
        print(email_string)
        print(f"\nTotal subscribers: {len(emails)}")

        # Print detailed info
        print("\nDetailed subscriber info:")
        print("------------------------")
        for sub in response.data:
            print(f"Name: {sub['name'] or 'Not provided'}, Email: {sub['email']}, Joined: {sub['date_added']}")

        # Save both formats to files
        with open('subscriber_emails.txt', 'w') as f:
            f.write(email_string)

        with open('subscriber_details.txt', 'w') as f:
            f.write("Name, Email, Date Added\n")
            for sub in response.data:
                f.write(f"{sub['name'] or 'Not provided'}, {sub['email']}, {sub['date_added']}\n")

        print("\nFiles saved:")
        print("- subscriber_emails.txt (comma-separated emails only)")
        print("- subscriber_details.txt (CSV with full details)")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    get_all_emails()
