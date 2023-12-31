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
  
  <p>test</p>
  <article class="prose">
    <h1>{post.title}</h1>
    <div>{@html htmlContent}</div> 
    <p>Created on: {post.date_created}</p>
    <p>Last Edited: {post.date_last_edited}</p>
  </article>
  