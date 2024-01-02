<script>
  import "../app.pcss";
</script>

<svelte:head>
  <title>Josh Shipton</title>
</svelte:head>

<nav
  class="absolute top-1 left-1/2 transform -translate-x-1/2 text-lg whitespace-nowrap py-1 gap-2 flex-row flex"
>
  <a href="/">home</a>
  •
  <a href="/collected-words">collected words</a>
  •
  <a href="/stream">thought stream</a>
  •
  <a href="/reach-me">reach me</a>
</nav>

<body>
  <slot />
</body>
