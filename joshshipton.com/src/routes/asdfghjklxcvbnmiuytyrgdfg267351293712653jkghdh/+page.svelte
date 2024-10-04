<div class="max-w-md mx-auto p-6">
    <h1 class="text-2xl font-bold mb-8 text-center">lol</h1>
    <form method="post" action="?/update" class="flex flex-col">
 
            <label for="quoteContent" >content:</label>
            <textarea id="quoteContent" class="border-black border-2" name="quoteContent" required 
                      rows="6" ></textarea>



            <label for="quoteAuthor">author:</label>
            <input class="border-black border-2" type="text" id="quoteAuthor" name="quoteAuthor" required />



            <label for="quoteSource" >source (if any):</label>
            <input class="border-black border-2" type="text" id="quoteSource" name="quoteSource" />


        <button type="submit" class= "my-4">
            submit
        </button>
    </form>
</div>