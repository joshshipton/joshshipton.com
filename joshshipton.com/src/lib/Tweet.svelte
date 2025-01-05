<script>
  export let text = ""; // The tweet text
  export let author = ""; // The author's Twitter handle
  export let authorName = ""; // The author's display name
</script>

<div class="custom-blockquote border-l-4 pl-4 py-2 my-4">
  <p>{text}</p>
  <div class="flex items-center mt-2">
    <span>- {authorName}</span>
    <img
      src={`https://x.com/${author}/photo`}
      alt="{authorName}'s profile picture"
      class="w-6 h-6 rounded-full ml-2"
    />
  </div>
</div>

<style>
  /* Scoped styling for the custom blockquote */
  .custom-blockquote {
    @apply italic bg-gray-100;
  }
</style>
