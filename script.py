folder_name = input("chuck us the name of the .md file: ")

with open(folder_name, 'r') as file:
    content =  file.readlines()

# need to change md into html here

new_name = folder_name.replace('.md', '.html')


with open(new_name,'w') as file:
    # writes the start of the head plus the title
    file.write("""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><link rel="stylesheet" type="text/css" href="style.css"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>`
    """ + content[0])
    # writes the rest of the head and the nav bar
    file.write("""</title></head><body><nav id="top-nav-bar"><p><a href="index.html">Home</a> • <a href="reach-me.html">Reach me</a> • <a href="blog-roll.html">Blogs I like</a> </p></nav>""")
    # now read the content from the thingo
    for i in range(2, len(content)):
        file.write(content[i])
    
    # close the html folder
    file.write("""</body></html>""")




print(f"HTML file '{new_name}' has been created from '{folder_name}'.")

print(content)