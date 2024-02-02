
<script>
    import { supabase } from "$lib/supabase";

    let content, author, source;
    let message = "";
    let submitting = false;

    async function submitForm() {
        submitting = true;
        message = "";

        const { data, error } = await supabase
            .from('quotes')
            .insert([{ content, author, source }]);

        if (error) {
            console.error('Error:', error);
            message = error.message;
        } else {
            console.log('Data submitted:', data);
            message = 'Quote submitted successfully!';
            content = author = source = '';
        }

        submitting = false;
    }
</script>

<div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Submit a Quote</h1>
    <form on:submit|preventDefault={submitForm} class="space-y-4">
        <div>
            <label for="content" class="block text-sm font-medium text-gray-700">Content</label>
            <textarea id="content" bind:value={content} required rows="4" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"></textarea>
        </div>
        <div>
            <label for="author" class="block text-sm font-medium text-gray-700">Author</label>
            <input type="text" id="author" bind:value={author} class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500">
        </div>
        <div>
            <label for="source" class="block text-sm font-medium text-gray-700">Source</label>
            <input type="text" id="source" bind:value={source} class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500">
        </div>
        <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">Submit</button>
    </form>
    {#if message}
        <p class="mt-4 text-green-500">{message}</p>
    {/if}
</div>
