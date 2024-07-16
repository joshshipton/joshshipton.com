<script>
  import { onMount } from "svelte";
  import { marked } from "marked";
  import Prism from "prismjs";
  import { tick } from "svelte";
  import "prismjs/components/prism-python";
  import "prismjs/themes/prism.css";
  import { supabase, getPublicImageUrl } from "$lib/supabase";

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


  renderer.image = (href, title, text) => {
  const imageUrl = getPublicImageUrl(href);
  return `<div class="center"><img src="${imageUrl}" alt="${text}" title="${title || ''}" class="my-4"></div>`;
};

  marked.setOptions({ renderer });

  export let data;
  const { post } = data;

  let htmlContent = "loading...";

  onMount(() => {
    // Convert Markdown to HTML
    htmlContent = marked.parse(post.post_content, {
      gfm: true,
      breaks: true,
    });

    // Apply syntax highlighting
    tick().then(() => {
      Prism.highlightAll();
      const links = document.querySelectorAll("a");
      links.forEach((link) => {
        const href = link.getAttribute("href");
        if (
          href &&
          href !== "/" &&
          href !== "/collected-words" &&
          href !== "/reach-me"
        ) {
          link.classList.add("link-wrapper");

          link.addEventListener("mouseover", () => {
            const tooltip = document.createElement("div");
            tooltip.classList.add("link-tooltip");
            tooltip.textContent = href;
            link.appendChild(tooltip);
          });

          link.addEventListener("mouseout", () => {
            const tooltip = link.querySelector(".link-tooltip");
            if (tooltip) {
              tooltip.remove();
            }
          });
        }
      });
    });
  });
</script>

<article class="prose">
  <p class="font-bold text-3xl text-left py-6 mt-6">{post.title}</p>
  <div>{@html htmlContent}</div>
  <p class="font-light text-sm py-6">Published on {post.date_created}</p>
</article>
