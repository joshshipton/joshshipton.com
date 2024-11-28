<script>
  import { onMount } from "svelte";
  import { enhance } from "$app/forms";
  console.log(`
   ____.            .__           .__    .__        __          
  |    | ____  _____|  |__   _____|  |__ |__|______/  |_  ____   ____       ____  ____   _____  
  |    |/  _ \\/  ___/  |  \\ /  ___/  |  \\|  \\____ \\   __\\/  _ \\ /    \\    _/ ___\\/  _ \\ /     \\ 
/\\__|    (  <_> )___ \\|   Y  \\___ \\|   Y  \\  |  |_> >  | (  <_> )   |  \\   \\  \\__(  <_> )  Y Y  \\
\\________|\\____/____  >___|  /____  >___|  /__|   __/|__|  \\____/|___|  / /\\ \\___  >____/|__|_|  /
                  \\/     \\/     \\/     \\/   |__|                    \\/  \\/     \\/            \\/ 
`);

  export let data;
  const { posts, popular_posts } = data;
  
</script>

<div>
  <p class="text-3xl font-bold text-center">JOSH SHIPTON INTERNET WEBSITE</p>
    <p class="text-xl font-semibold text-center py-4">tech</p>

  <div class="flex flex-col mx-4 gap-2">
    <p class="text-xl font-semibold text-center py-4">recent posts</p>

    {#each posts as post}
      <div>
        <a href={`/post/${post.post_link}`}>
          <p class="text-lg font-bold text-left hover:underline">
            {post.title}
          </p>

          <p class="text-sm text-light text-left">{post.date_created}</p>
          <p class="text-sm text-left">{post.content_peek}...</p>
        </a>
      </div>
    {/each}
    <p><a href="/all-posts">see all...</a></p>
  </div>

  <div class="flex flex-col mx-4 gap-2">
    <p class="text-xl font-semibold text-center py-4">popular posts</p>
    {#each popular_posts as post}
      <div>
        <a href={`/post/${post.post_link}`}>
          <p class="text-lg font-bold text-left hover:underline">
            {post.title}
          </p>
          <p class="text-sm text-light text-left">{post.date_created}</p>
          <p class="text-sm text-left">{post.content_peek}...</p>
        </a>
      </div>
    {/each}
  </div>
</div>
