#!/usr/bin/env python

import sys

# Smart quotes mapping
smart_quotes_mapping = {
    '‘': "'",  # Left single quotation mark to plain single quote
    '’': "'",  # Right single quotation mark to plain single quote
    '“': '"',  # Left double quotation mark to plain double quote
    '”': '"'   # Right double quotation mark to plain double quote
}

# Replace smart quotes in a string
def replace_smart_quotes(text):
    for smart, plain in smart_quotes_mapping.items():
        text = text.replace(smart, plain)
    return text

# Main function to process the text file and convert it to HTML
def main(argv):
    # Do something with argv
    print(f"Received arguments: {argv}")

    try:
        folder_name = argv[0]
    except IndexError:
        return print("Correct usage: ./script {input.txtfile}")

    try:
        with open(folder_name, 'r', encoding='utf-8') as file:
            content = file.readlines()
    except FileNotFoundError:
        return print("File not found. Make sure the path is correct.")

    # Replace smart quotes in content
    content = [replace_smart_quotes(item.strip()) for item in content if item.strip() != ""]

    if len(content) < 2:
        return print("The input file does not have enough lines for title and date.")

    new_name = folder_name.replace('.txt', '.html')
    title = content[0]
    date = content[1]

    with open(new_name, 'w', encoding='utf-8') as file:
        file.write("""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><link rel="stylesheet" type="text/css" href="style.css"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>"""
        + new_name + """</title></head><body>""")

        file.write(f"<h1 id='title'>{title}</h1>")

        for i in range(2, len(content)):
            if content[i].startswith("HEADER"):
                file.write(f"<h3>{content[i][7:]}</h3>")
            else:
                file.write(f"<p>{content[i]}</p>")

        file.write(f"<p>Published on {date} </p>")

        file.write("""</body><script src="js/app.js"></script></html>""")

    print(f"HTML file '{new_name}' has been created from '{folder_name}'.")
    print("Updating Json Object Now")
    print(",{" + f"'title': '{title}', 'link': '/{new_name}', 'date': '{date}', 'peek': '{content[2][:75]}'" + "}")

# Check if the script is the main program and execute
if __name__ == "__main__":
    main(sys.argv[1:])
