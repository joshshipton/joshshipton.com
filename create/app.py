# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Load environment variables and setup Supabase
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
POSTS_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'posts')
LINKS_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'links')
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def create_post_file(title, content):
    """Create a new post file with proper metadata structure"""
    # Clean the title to create a URL-friendly link
    link = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"{timestamp}-{link}.md"

    # Ensure posts directory exists
    if not os.path.exists(POSTS_DIRECTORY):
        os.makedirs(POSTS_DIRECTORY)

    # Create the full post content with metadata
    post_content = f"""ID=""
TITLE="{title}"
LINK="{link}"
IS_DRAFT=T
IS_POPULAR=F
----------
{content}"""

    # Create the full file path
    filepath = os.path.join(POSTS_DIRECTORY, filename)
    print(f"Creating post file at: {filepath}")  # Debug print

    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(post_content)

    return filepath

@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        try:
            # Create the post file
            filepath = create_post_file(title, content)
            print(f"Post file created at: {filepath}")  # Debug print

            # Try to push it to Supabase immediately
            try:
                from push_post import parse_post, upload_post_to_supabase
                post_data, header = parse_post(filepath)
                post_data['header'] = header
                upload_post_to_supabase(filepath, post_data)
                flash('Post created and pushed to Supabase successfully!', 'success')
            except Exception as e:
                flash(f'Post file created but not pushed: {str(e)}', 'warning')

            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error creating post: {str(e)}', 'error')
            print(f"Error creating post: {str(e)}")  # Debug print

    return render_template('new_post.html')

def get_all_posts():
    response = supabase.table("posts").select("*").execute()
    return response.data

def get_all_quotes():
    response = supabase.table("quotes").select("*").execute()
    return response.data

def get_post_by_id(post_id):
    response = supabase.table("posts").select("*").eq('id', post_id).execute()
    return response.data[0] if response.data else None

def get_post_file_path(post_id):
    # Scan the posts directory for the file with matching ID
    for filename in os.listdir(POSTS_DIRECTORY):
        if filename.endswith('.md'):
            with open(os.path.join(POSTS_DIRECTORY, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                if f'ID="{post_id}"' in content:
                    return os.path.join(POSTS_DIRECTORY, filename)
    return None

def update_post_file(filepath, title, content, link=None, is_draft='T', is_popular='F'):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Get the ID from existing file
    id_line = next(line for line in lines if line.startswith('ID='))
    post_id = id_line.split('"')[1]

    # If no link provided, generate from title
    if not link:
        link = re.sub(r'[^a-zA-Z0-9]', '-', title.lower())

    # Create updated content
    updated_content = f'''ID="{post_id}"
TITLE="{title}"
LINK="{link}"
IS_DRAFT={is_draft}
IS_POPULAR={is_popular}
----------
{content}'''

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return post_id

@app.route('/')
def index():
    posts = get_all_posts()
    quotes = get_all_quotes()
    links = supabase.table("links").select("*").order('date', desc=True).execute().data
    
    search_query = request.args.get('search', '').lower()
    if search_query:
        posts = [p for p in posts if search_query in p['title'].lower() or search_query in p['content_peek'].lower()]
        quotes = [q for q in quotes if search_query in q['content'].lower() or search_query in q['author'].lower()]
        links = [l for l in links if search_query in l['content'].lower()]
    
    return render_template('index.html', posts=posts, quotes=quotes, links=links)


app.route('/api/search')
def api_search():
    search_query = request.args.get('q', '').lower()
    posts = get_all_posts()
    quotes = get_all_quotes()
    links = supabase.table("links").select("*").execute().data
    
    if search_query:
        posts = [p for p in posts if search_query in p['title'].lower() or 
                (p['content_peek'] and search_query in p['content_peek'].lower())]
        quotes = [q for q in quotes if search_query in q['content'].lower() or 
                 search_query in q['author'].lower()]
        links = [l for l in links if search_query in str(l['date']).lower() or 
                (l['content'] and search_query in l['content'].lower())]
    
    return jsonify({'posts': posts, 'quotes': quotes, 'links': links})


@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = get_post_by_id(post_id)
    if not post:
        flash('Post not found', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        is_draft = request.form.get('is_draft', 'T')
        is_popular = request.form.get('is_popular', 'F')

        try:
            filepath = get_post_file_path(post_id)
            if not filepath:
                flash('Post file not found', 'error')
                return redirect(url_for('index'))

            update_post_file(filepath, title, content, post['post_link'], is_draft, is_popular)
            flash('Post updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error updating post: {str(e)}', 'error')

    filepath = get_post_file_path(post_id)
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract content after the metadata
            content = content.split('----------\n')[1] if '----------\n' in content else content
    else:
        content = post.get('post_content', '')

    return render_template('edit_post.html', post=post, content=content)

@app.route('/quote/new', methods=['GET', 'POST'])
def new_quote():
    if request.method == 'POST':
        content = request.form['content']
        author = request.form['author']
        source = request.form['source'] or None

        try:
            data = {'content': content, 'author': author, 'source': source}
            supabase.table("quotes").insert(data).execute()
            flash('Quote added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error adding quote: {str(e)}', 'error')

    return render_template('new_quote.html')

@app.route('/post/<int:post_id>/push')
def push_post(post_id):
    try:
        # Get the file path
        filepath = get_post_file_path(post_id)
        if not filepath:
            flash('Post file not found', 'error')
            return redirect(url_for('index'))

        # First update the file to set IS_DRAFT=F
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace IS_DRAFT=T with IS_DRAFT=F in the content
        content = content.replace('IS_DRAFT=T', 'IS_DRAFT=F')

        # Write the updated content back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        # Now push to Supabase
        from push_post import parse_post, upload_post_to_supabase
        post_data, header = parse_post(filepath)
        post_data['header'] = header
        upload_post_to_supabase(filepath, post_data)

        flash('Post pushed to Supabase successfully!', 'success')
    except Exception as e:
        flash(f'Error pushing post: {str(e)}', 'error')
    return redirect(url_for('index'))



@app.route('/delete/post/<int:post_id>')
def delete_post(post_id):
    try:
        filepath = get_post_file_path(post_id)
        if filepath:
            os.remove(filepath)
        supabase.table("posts").delete().eq('id', post_id).execute()
        flash('Post deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting post: {str(e)}', 'error')
    return redirect(url_for('index'))

@app.route('/delete/quote/<int:quote_id>')
def delete_quote(quote_id):
    try:
        supabase.table("quotes").delete().eq('id', quote_id).execute()
        flash('Quote deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting quote: {str(e)}', 'error')
    return redirect(url_for('index'))


# app.py (update these functions)

def create_links_file(date, intro, content_items, is_draft=True):
    """Create a new links file with structured content"""
    # Use current date if none provided
    if not date:
        date = datetime.now()
    elif isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')
    
    # Generate the link from date
    link = date.strftime("%d-%m-%Y")
    filename = f"{link}.md"
    
    # Create the content sections
    sections = {
        'articles': [],
        'videos': [],
        'tweets': [],
        'books': [],
        'papers': [],
        'other': []
    }
    
    for item in content_items:
        sections[item['type']].append(item)
    
    # Build the markdown content
    content = f"# Links for {date.strftime('%d-%m-%Y')}\n"
    content += f'LINK="{link}"\n'
    content += f'IS_DRAFT={"T" if is_draft else "F"}\n'
    content += "----------\n\n"
    
    # Add intro if provided
    if intro:
        content += f"{intro}\n\n"
    
    # Add non-empty sections
    if sections['articles']:
        content += "## Articles & Essays\n"
        for article in sections['articles']:
            content += f"#### [{article['title']}]({article['url']})\n{article['description']}\n\n"
    
    if sections['videos']:
        content += "## Videos\n"
        for video in sections['videos']:
            content += f"#### [{video['title']}]({video['url']})\n"
            content += video['embed_code'] + "\n"
            content += f"{video['description']}\n\n"
    
    if sections['tweets']:
        content += "## Tweets\n"
        for tweet in sections['tweets']:
            content += tweet['embed_code'] + "\n"
            content += f"{tweet['description']}\n\n"
    
    if sections['books']:
        content += "## Books\n"
        for book in sections['books']:
            content += f"#### [{book['title']}]({book['url']})\n{book['description']}\n\n"
    
    if sections['papers']:
        content += "## Papers & Research\n"
        for paper in sections['papers']:
            content += f"#### [{paper['title']}]({paper['url']})\n{paper['description']}\n\n"
    
    if sections['other']:
        content += "## Other Cool Finds\n"
        for other in sections['other']:
            content += f"#### [{other['title']}]({other['url']})\n{other['description']}\n\n"
    
    # Save the file
    filepath = os.path.join(LINKS_DIRECTORY, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath, link, date, content

@app.route('/link/<int:link_id>/delete')
def delete_link(link_id):
    try:
        # Get the link data first
        response = supabase.table("links").select("*").eq('id', link_id).execute()
        if not response.data:
            flash('Link not found', 'error')
            return redirect(url_for('index'))
        
        link = response.data[0]
        
        # Delete the file
        filepath = os.path.join(LINKS_DIRECTORY, f"{link['links_link']}.md")
        if os.path.exists(filepath):
            os.remove(filepath)
        
        # Delete from Supabase
        supabase.table("links").delete().eq('id', link_id).execute()
        
        flash('Link deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting link: {str(e)}', 'error')
    
    return redirect(url_for('index'))


def create_links_file(date, intro, content_items, is_draft=True):
    """Create a new links file with structured content"""
    # Use current date if none provided
    if not date:
        date = datetime.now()
    elif isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')
    
    # Generate the link from date
    link = date.strftime("%d-%m-%Y")
    filename = f"{link}.md"
    
    # Create the content sections
    sections = {
        'articles': [],
        'videos': [],
        'tweets': [],
        'books': [],
        'papers': [],
        'other': []
    }
    
    for item in content_items:
        if item.get('title') or item.get('description') or item.get('embed_code'):
            sections[item['type']].append(item)
    
    # Build the markdown content
    content = [f"# Links for {date.strftime('%d-%m-%Y')}"]
    content.append(f'LINK="{link}"')
    content.append(f'IS_DRAFT={"T" if is_draft else "F"}')
    content.append("----------\n")
    
    # Add intro if provided
    if intro:
        # Preserve any HTML in the intro
        content.append(f"{intro.strip()}\n")
    
    # Add non-empty sections
    if sections['articles']:
        content.append("## Articles & Essays")
        for article in sections['articles']:
            title = article['title'].strip()
            url = article['url'].strip()
            desc = article['description'].strip()
            content.append(f"#### [{title}]({url})")
            content.append(f"{desc}\n")
    
    if sections['videos']:
        content.append("## Videos")
        for video in sections['videos']:
            title = video['title'].strip()
            url = video['url'].strip()
            desc = video['description'].strip()
            embed = video['embed_code'].strip() if video.get('embed_code') else ''
            content.append(f"#### [{title}]({url})")
            if embed:
                content.append(embed)
            content.append(f"{desc}\n")
    
    if sections['tweets']:
        content.append("## Tweets")
        for tweet in sections['tweets']:
            if tweet.get('embed_code'):
                content.append(tweet['embed_code'].strip())
            if tweet.get('description'):
                content.append(f"{tweet['description'].strip()}\n")
    
    # Join all content with proper line breaks
    final_content = '\n'.join(content)
    
    # Ensure posts directory exists
    os.makedirs(LINKS_DIRECTORY, exist_ok=True)
    
    # Save the file
    filepath = os.path.join(LINKS_DIRECTORY, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    return filepath, link, date, final_content

@app.route('/links/new', methods=['GET', 'POST'])
def new_links():
    if request.method == 'POST':
        date = request.form.get('date')
        intro = request.form.get('intro', '').strip()
        action = request.form.get('action', 'save')
        is_draft = (action == 'save')
        
        content_items = []
        # Group form fields into content items
        types = request.form.getlist('type[]')
        titles = request.form.getlist('title[]')
        urls = request.form.getlist('url[]')
        descriptions = request.form.getlist('description[]')
        embeds = request.form.getlist('embed[]')
        
        # Zip all the fields together
        for i in range(len(types)):
            type_key = types[i] if i < len(types) else ''
            if type_key and (i < len(titles) or i < len(descriptions) or i < len(embeds)):
                item = {
                    'type': type_key,
                    'title': titles[i] if i < len(titles) else '',
                    'url': urls[i] if i < len(urls) else '',
                    'description': descriptions[i] if i < len(descriptions) else '',
                    'embed_code': embeds[i] if i < len(embeds) else ''
                }
                # Only add items that have some content
                if item['title'] or item['description'] or item['embed_code']:
                    content_items.append(item)
        
        try:
            filepath, link, date, content = create_links_file(date, intro, content_items, is_draft)
            
            if not is_draft:
                # Push to Supabase only if publishing
                data = {
                    'date': date.strftime('%Y-%m-%d'),
                    'content': content,
                    'links_link': link
                }
                supabase.table("links").insert(data).execute()
                flash('Links created and published!', 'success')
            else:
                flash('Links saved as draft!', 'success')
            
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error creating links: {str(e)}', 'error')
            print(f"Error details: {str(e)}")  # For debugging
    
    return render_template('new_links.html', today=datetime.now().strftime('%Y-%m-%d'))


@app.route('/link/<int:link_id>/edit', methods=['GET', 'POST'])
def edit_link(link_id):
    try:
        # Get link data from Supabase
        response = supabase.table("links").select("*").eq('id', link_id).execute()
        if not response.data:
            flash('Link not found', 'error')
            return redirect(url_for('index'))
        
        link = response.data[0]
        
        if request.method == 'POST':
            try:
                # Get the updated content directly from the form
                updated_content = request.form.get('content', '')
                
                # Update Supabase
                supabase.table("links").update({
                    'content': updated_content
                }).eq('id', link_id).execute()
                
                # Find and update the corresponding file if it exists
                link_filename = f"{link['links_link']}.md"
                filepath = os.path.join(LINKS_DIRECTORY, link_filename)
                if os.path.exists(filepath):
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                
                flash('Link updated successfully!', 'success')
                return redirect(url_for('index'))
            except Exception as e:
                flash(f'Error updating link: {str(e)}', 'error')
                return redirect(url_for('index'))
        
        # For GET request, just show the current content
        return render_template('edit_link.html', link=link)
    
    except Exception as e:
        flash(f'Error accessing link: {str(e)}', 'error')
        return redirect(url_for('index'))


if __name__ == '__main__':
    # Ensure posts directory exists when starting the app
    if not os.path.exists(POSTS_DIRECTORY):
        os.makedirs(POSTS_DIRECTORY)
    app.run(debug=True)
