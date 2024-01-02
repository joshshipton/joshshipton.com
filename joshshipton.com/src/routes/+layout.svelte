<script>
  import "../app.pcss";
</script>

<svelte:head>
  <title>Josh Shipton</title>
</svelte:head>

<nav
  class="absolute top-1 left-1/2 transform -translate-x-1/2 text-lg whitespace-nowrap py-1 gap-1 flex-row flex sm:text-sm md:text-base lg:text-lg"
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
