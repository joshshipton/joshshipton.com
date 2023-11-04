#!/usr/bin/env python
import sys
import supabase_py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# loads .env
load_dotenv()


# Function to generate the full link from a given filename
def get_link(filename):
    base_url = 'joshshipton.com/'  # Replace with your website's base URL
    link = base_url + filename
    return link

def get_data_from_supabase():
<<<<<<< HEAD
    url: str = 'https://rdxhiwxfooidvexdrgxs.supabase.co'  # Replace with your actual Supabase URL
=======
    url: str = 'https://your-supabase-url.supabase.co'  # Replace with your actual Supabase URL
>>>>>>> dcc6619cb3b60871b1aad08e84474741ec03a81d
    key: str = os.getenv('SUPABASE_KEY')  # Make sure this matches the environment variable storing your Supabase key
    supabase = supabase_py.create_client(url, key)
    
    response = supabase.table('emails').select('email').execute()
    
<<<<<<< HEAD
    # Check if there is an error key in the response
    if 'error' in response:
        # Handle any errors - print the error message and return an empty list
        print(f"Error: {response['error']}")
        return []
    else:
        # Assume the response contains the data directly if there's no error
        email_data = response['data']
        emails = [item['email'] for item in email_data]
        print(emails)
        return emails


=======
    # Check the response status code
    if response.status_code == 200:
        # Extract the email data from the response
        email_data = response.json()  # Parse the JSON response into a dictionary
        emails = [item['email'] for item in email_data]
        print(emails)
        return emails
    else:
        # Handle any errors - print the error message and return an empty list
        print(f"Error: {response.status_code}, {response.text}")
        return []

>>>>>>> dcc6619cb3b60871b1aad08e84474741ec03a81d
# Function to send emails to a list of email addresses


def send_emails(email_list, link):
    smtp_server = 'smtp.gmail.com'  # Gmail's SMTP server
    smtp_port = 587  # TLS port for SMTP
    smtp_user = 'shiptonjosh@gmail.com'
    smtp_password = os.environ.get('GMAIL_PASSWORD')

    message = MIMEMultipart()
    message['Subject'] = 'New post'
    message['From'] = smtp_user
    message.attach(
        MIMEText(f'New post, you can read it here: {link} :)', 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)

    for email in email_list:
      # Copy the message for each recipient to set the 'To' field individually
        print("Sending to email: ")
        print(email)
        msg = message.copy()
        msg['To'] = email
        server.sendmail(smtp_user, email, msg.as_string())

    server.quit()

<<<<<<< HEAD
def print_emails(lst):
   print("\n-=-=-=-=-=-=-=-=-=-=-=-=-")

   for email in lst:
        print(email, end=" ")
   print("\n-=-=-=-=-=-=-=-=-=-=-=-=-")

=======
>>>>>>> dcc6619cb3b60871b1aad08e84474741ec03a81d

def main(filename):
    link = get_link(filename)
    email_list = get_data_from_supabase()
<<<<<<< HEAD
    print_emails(email_list)
   #  doesnt work but at least I can pull all the emails 
   #  send_emails(email_list, link)
=======
    send_emails(email_list, link)
>>>>>>> dcc6619cb3b60871b1aad08e84474741ec03a81d


if __name__ == "__main__":
    print("running")
    if len(sys.argv) > 1: 
        filename = sys.argv[1]  
        main(filename)
    else:
        print("No filename provided.")
    print("done?")
