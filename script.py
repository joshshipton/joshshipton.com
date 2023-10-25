#!/usr/bin/env python

import sys

#usage ./script {.txt file}
def main(argv):
    # Do something with argv
    print(f"Received arguments: {argv}")

    try:
        folder_name = argv[0]
    except ValueError:
        return print("Correct usage: ./script {.txtfile}")

    try:
        with open(folder_name, 'r', encoding='utf-8') as file:
            content = file.readlines()
    except FileNotFoundError:
        return print("Correct usage: ./script {.txtfile}")

    new_name = folder_name.replace('.txt', '.html')

    content = [item.strip() for item in content if item.strip() != ""]
    title = content[0]
    date = content[1]

    with open(new_name, 'w') as file:
        file.write("""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><link rel="stylesheet" type="text/css" href="style.css"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>"""
        + new_name + """</title></head><body>""")
        
        file.write(f"<h1 id='title'>{title}</h1>")
        
        for i in range(2, len(content)):
            if content[i].startswith("HEADER"):
                file.write(f"<h3>{content[i][7:]}</h3>")
            else:
                file.write(f"<p>{content[i]}</p>")
                
        file.write(f"<p>Published on {date} </p>")
        
        file.write("""</body><script src="app.js"></script></html>""")

    print(f"HTML file '{new_name}' has been created from '{folder_name}'.")
    print("Updating Json Object Now")
    print(",{" + f"'title': '{title}', 'link': '/{new_name}', 'date': '{date}', 'peek': '{content[2][:50]}'" + "}")


if __name__ == "__main__":
    main(sys.argv[1:])