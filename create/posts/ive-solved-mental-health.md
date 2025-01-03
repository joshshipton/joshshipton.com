ID=""
TITLE=""
LINK=""
IS_DRAFT=T
IS_POPULAR=F
----------

journalling workflow, i'm a big fan of journalling i think writing down your thoughts and beliefs is a good way to make sure that they are based in fact and logical. it's a good way of truley understanding your problems and i find that when i journal i probably have more agency and better executive function due to the fact that i have processed more feelings/thoughts and am more clear with myself about how i truley feel about things. 

this is all standard.

however something i'm really excited about is the use of LLM's (particuallry models like claude who seem more personal) to provide un-biased non-judgemental feedback on your inner thoughts and feelings. 

i've always journalled mostly with pen and paper however and sometimes used my laptop for the occasional entry, with my journal synced using git to track changes and manage across different devices. 

i've recently switched to doing almost all of my daily journalling on my laptop and have a nice linux script that easily creates the file, lets me edit it and then saves it to github (included below if you want it) 

my thinking here is that it includes a written record of my thoughts, how i am thinking, and how my thinking evoles over time, this is easily then given to claude and then as models get better and better it will be able to notice more and more nuanced patterns in my thinking. 



## Problems i'm running into

too much information, i write a lot. there is too much information for the LLM. 
possible solutions 

- wait for llm's to have larger context windows
- split up the entires into managable chunks 
- try and increase token density (summarize entires) 
- convert everything into embeddings 

essentially the main thing we are doing here is increasing token density. 

out of all of these tricks only embeddings really makes sense to me, using an llm to summarize and then asking it to summarize the summarize seems like we are going to lose a lot of nuance and is not something i am intrested in or can be bothered to do right now, maybe in the future. would be simple to implement, just summarize each entry with some llm before appending it to the big text file, repeat for all entries. before giving th3e summarization of summarizationt to the llm. 

before we do complex stuff like embeddings i researched simple tricks to increase token density, some of the simplest ones i found were; 

- remove redundant whitespace, whitespace counts as tokens. rwemove extra spaces, tabs and newlines. 
- bullet points instead of paragraphs (this would involve conciouslly changing how i write which i am against for this project) 
- remove stop words e.g "the", "a", "is", they dont do much to convey information but consume valuable tokens
- combining sentences, seperate sentences use more tokens. e.g "It rained toady. so i stayed inside." -> "it rained, i stayed inside. (the second sentence uses less tokens)

of these whitespace and removing stop words make the most sense. i'll keep the orignal script that does not change the journal entires other than removing excess new lines at the bottom but also include another script that does more hardcore token densificatiuon (is this the right word? idk,) 

the new script will remove common stop words as well as spaces. 


### Results 

for the not token densified version the results are ok. claude is able to pick up on general theems 

### Next steps 

next i want to try using the journal entries as a data-set. i have absoltely no clue how to do this but should be a good time. 


<div class="center">  <h2> ~~~ Code ~~~ </h2> </div> 

bash script to add to .bashrc to easily spin up a new journal entry
~~~bash
# quick command to push code to git
alias x='git add . && git commit -m "code go brr" && git push'

# gm command (short for good morning) to quickly start a new journal entry
gm() {
    local journal_dir="$HOME/personal_journal/daily"
    local template_file="$journal_dir/template.md"
    local current_date
    local new_file

    current_date=$(date +%Y-%m-%d)
    new_file="$journal_dir/${current_date}.md"

    # Check if template exists
    if [ ! -f "$template_file" ]; then
        echo "Error: Template file '$template_file' does not exist."
        return 1
    fi

    # Create new journal entry if it doesn't exist
    if [ ! -f "$new_file" ]; then
        cp "$template_file" "$new_file"
        local current_time=$(date +%H:%M:%S)
        {
            echo "Time: $current_time"
            echo
            cat "$template_file"
        } > "$new_file"
    fi

    # Open the journal file in nvim
    nvim "$new_file"

    # Save changes to git 
    if command -v x >/dev/null 2>&1; then
        x || echo "Warning: Failed to push changes to Git."
    else
        echo "Error: 'x' command not found."
    fi
}

~~~

script without hardcore token density optimizations, removes some extra whitespace but doesnt change the content of the entires at all

~~~python

import os
from datetime import datetime
import re

"""
This is a python script to take all of my jounral entries (which are .md files) and append them all to a single .txt file which i can then give to an LLM for free therapy. 

Future Improvements: 
    Select a specific date and time range 
    Add direct api call to the llm of choice
"""

def get_creation_time(file_path):
    try:
        # Get file stats
        stats = os.stat(file_path)
        # Use st_ctime for creation time (or status change time on Unix-like systems)
        creation_time = stats.st_ctime
        # Convert to readable timestamp
        return datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(f"Error retrieving creation time for {file_path}: {e}")
        return "Unknown"


def makebook(output_file):
    # Get the current directory
    current_dir = os.getcwd()
    thoughts_dir = os.path.join(current_dir, "thoughts")
    daily_dir = os.path.join(current_dir, "daily")
    
    # Collect all .md files from the two directories
    md_files = []
    if os.path.exists(thoughts_dir):
        md_files.extend([os.path.join(thoughts_dir, f) for f in os.listdir(thoughts_dir) if f.endswith('.md')])
    if os.path.exists(daily_dir):
        md_files.extend([os.path.join(daily_dir, f) for f in os.listdir(daily_dir) if f.endswith('.md')])
    

    print(f"Found {len(md_files)} Markdown files.")
    
    if not md_files:
        print("No .md files found in the current directory.")
        return
    
    # Open the output file for writing
    with open(output_file, 'w', encoding='utf-8') as output:
        # the file names are actually paths here
        for file_name in md_files:
            try:
                # Read the content of the file
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Process the content to clean up whitespace
                processed_lines = []
                for line in content.split('\n'):
                    # Check if the line is a heading
                    if re.match(r'^#+\s', line):
                        # Add a newline before headings to ensure proper separation
                        processed_lines.append('\n' + line.strip())
                    elif line.strip():
                        # For non-empty, non-heading lines, append without newline
                        processed_lines.append(line.strip())
                
                # Write the header and processed content to the output file
                timestamp = get_creation_time(file_name)
                output.write(f"-----\nFile: {file_name}\nDate: {timestamp}\n-----\n")
                output.write('\n'.join(processed_lines))
                output.write("\n")  
            
            except Exception as e: print(f"Error reading file '{file_name}': {e}")
    
    print(f"All .md files in the current directory have been concatenated into '{output_file}'.")

# Define the output file name
output_file = "output.txt"

# Run the script
makebook(output_file)
~~~

python script with more hardccore opeimations 

