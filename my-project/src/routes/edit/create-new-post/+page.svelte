<script>
    import { onMount } from 'svelte';
    import marked from 'marked';

    let markdownContent = '';
    let renderedContent = '';

    onMount(() => {
        updateRenderedContent();
    });

    function updateRenderedContent() {
        renderedContent = marked(markdownContent);
    }
</script>

<div class="flex flex-row h-screen">
    <div class="flex-1 p-4 overflow-auto">
        <textarea class="w-full h-full" bind:value={markdownContent} on:input={updateRenderedContent}></textarea>
    </div>
    <div class="flex-1 p-4 overflow-auto bg-gray-100">
        {@html renderedContent}
    </div>
</div>

<style>
    textarea {
        resize: none;
    }
</style>

    