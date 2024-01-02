<script>
  export let data;
  const { posts } = data;
  console.log(posts);
</script>
<div>
<p class="text-3xl font-bold text-center">Hi!</p>
<p class="text-sm text-center">
  I'm Josh, I made a blog because <a href="/post/why-blog">people</a> on
  the internet told me it was a good idea. (I'm easily influenced)
</p>
<div class="flex flex-col mx-4 gap-2">
  <p class="text-xl font-semibold text-center py-4">Recent Posts</p>
  {#each posts as post}
    <div>
      <a href={`/post/${post.post_link}`}>
        <p class="text-lg font-bold text-left hover:underline" >{post.title}</p>


        <p class="text-sm text-light text-left">{post.date_created}</p>
        <p class="text-sm text-left">{post.content_peek}...</p>
      </a>
    </div>
  {/each}
</div>
</div>

