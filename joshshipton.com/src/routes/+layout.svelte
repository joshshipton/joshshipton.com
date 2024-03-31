<script>
  import "../app.pcss";
</script>

<svelte:head>
  <title>Josh Shipton</title>
</svelte:head>

<nav 
 class="absolute top-0 left-1/2 transform -translate-x-1/2 whitespace-nowrap text-md md:text-base lg:text-lg">



  <a href="/">home</a>
  •
  <a href="/collected-words">word collection</a>
  •
  <!-- <a href="/stream">thought stream</a>
  • -->
  <a href="/reach-me">reach me</a>
</nav>
<body>
  <slot />
</body>
