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

~~~bash
    
alias x='git add . && git commit -m "code go brr" && git push'
 
### Script to open and start new daily journal entry
gm() {
        local input_file="~/personal_journal/daily/template.md"
        input_file=$(eval echo "$input_file") 
 
        if [ ! -f "$input_file" ]; then
                echo "Error: File '$input_file' does not exist."
                return 1
        fi   
 
        local current_date
        current_date=$(date +%Y-%m-%d)
        local new_file="${current_date}.md"
        
        # if the file hasn't been created yet
        if [ ! -f "$new_file" ]; then
                cp "$input_file" "$new_file"
                local current_time=$(date +%H:%M:%S)
        {
        echo "Time: $current_time"
        echo
        cat "$input_file"
        } > "$new_file"
 
    fi
  
    # open either the file that already exists or the new file 
    nvim "$new_file"
 
    # my other script that just pushes code directly to github (saves the journal) 
    x
 
}

~~~

