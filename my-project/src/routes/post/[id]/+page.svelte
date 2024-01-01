<script>
    import { onMount } from "svelte";
    import { marked } from "marked";
  
    export let data;
    const { post } = data;
  
    let htmlContent;
  
    onMount(() => {
      // Convert Markdown to HTML
      htmlContent = marked.parse(post.post_content, {
        gfm: true,
        breaks: true,
      });
    });
  </script>
  
  <article class="prose">
    <p class="font-bold text-3xl text-left py-6 mt-6">{post.title}</p>
    <div>{@html htmlContent}</div> 
    <p class="font-light text-sm py-6">{post.date_created}</p>

  </article>
  