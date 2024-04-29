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
      const listClass = ordered ? "ordered-list-class" : "unordered-list-class"; // Add custom classes if needed
      return `<${type} class="${listClass} px-1">${body}</${type}>`;
    };
  
    // Custom rendering for list items
    renderer.listitem = (text) => {
      return `<li>${text}</li>`;
    };
  
    // Custom rendering for bold text
    renderer.strong = (text) => {
      return `<strong class="font-semibold">${text}</strong>`;
    };
  
    marked.setOptions({ renderer });
  
    export let data;
    const { post } = data;
  
    let htmlContent;
  
    onMount(() => {
      // Convert Markdown to HTML
      htmlContent = marked.parse(post.content, {
        gfm: true,
        breaks: true,
      });
  
    });
  </script>
  
  <article class="prose">
    <p class="font-bold text-3xl text-left py-6 mt-6">Links by Today {post.date}</p>
    <div>{@html htmlContent}</div>
  </article>
  