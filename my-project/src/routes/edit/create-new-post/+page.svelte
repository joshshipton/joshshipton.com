<script>
  import { onMount } from "svelte";
  import { marked } from "marked";

  const renderer = new marked.Renderer();

  // Custom rendering for headers
  renderer.heading = (text, level) => {
    const sizes = [
      "text-2xl",
      "text-xl",
      "text-lg",
      "text-md",
      "text-sm",
      "text-xs",
    ];
    return `<h${level} class="${
      sizes[level - 1]
    } font-semibold my-2">${text}</h${level}>`;
  };

  // Custom rendering for blockquotes
  renderer.blockquote = (quote) => {
    return `<blockquote class="border-l-4 border-gray-200 pl-4 italic my-4">${quote}</blockquote>`;
  };

  // Custom rendering for lists
  renderer.list = (body, ordered) => {
    const type = ordered ? "ol" : "ul";
    return `<${type} class="list-inside list-disc pl-5 my-2">${body}</${type}>`;
  };

  // Custom rendering for list items
  renderer.listitem = (text) => {
    return `<li class="my-1">${text}</li>`;
  };

  // Custom rendering for bold text
  renderer.strong = (text) => {
    return `<strong class="font-semibold">${text}</strong>`;
  };

  marked.setOptions({ renderer });

  let markdownContent = "";
  let renderedContent = "";

  onMount(() => {
    updateRenderedContent();
  });

  function updateRenderedContent() {
    renderedContent = marked(markdownContent);
  }
</script>

<div class="flex flex-row h-screen">
  <div class="flex-1 p-4 overflow-auto">
    <textarea
      class="w-full h-full"
      bind:value={markdownContent}
      on:input={updateRenderedContent}
    ></textarea>
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
