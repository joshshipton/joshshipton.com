<script>
  import { page } from "$app/stores";
</script>

<div class="flex flex-col justify-center items-center mt-4">
  <p class="text-4xl py-10"><strong>Something went wrong</strong></p>
  <p>Here's the error if that means something to you.</p>
    <h2>{$page.status}</h2>
    <p class="subhead">{$page.error.message}</p>
  <p>
    Maybe go <a href="/">home?</a>
  </p>
</div>
