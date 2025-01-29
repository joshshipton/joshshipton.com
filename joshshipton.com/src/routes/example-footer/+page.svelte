<!-- +page.svelte -->
<script>
  import { PalmtreesIcon, PlaneIcon, GlobeIcon } from 'lucide-svelte';
</script>

<div class="min-h-screen flex flex-col">
  <main class="flex-1 max-w-3xl mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">Travel Experiences</h1>

    <div class="space-y-8">
      <!-- Section 1 -->
      <div class="flex items-center gap-4 mb-4">
        <PalmtreesIcon class="w-8 h-8 text-gray-600" />
        <h2 class="text-xl font-semibold">Luxury Resorts</h2>
      </div>
      <p class="text-gray-600">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
        nostrud exercitation ullamco laboris.
      </p>

      <!-- Section 2 -->
      <div class="flex items-center gap-4 mb-4">
        <PlaneIcon class="w-8 h-8 text-gray-600" />
        <h2 class="text-xl font-semibold">Flight Reviews</h2>
      </div>
      <p class="text-gray-600">
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
        eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.
      </p>

      <!-- Section 3 -->
      <div class="flex items-center gap-4 mb-4">
        <GlobeIcon class="w-8 h-8 text-gray-600" />
        <h2 class="text-xl font-semibold">Global Adventures</h2>
      </div>
      <p class="text-gray-600">
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet.
      </p>
    </div>
  </main>

  <!-- Footer -->
  <footer class="py-4 text-center text-xs">
    <p>Website by <a href="mailto:shiptonjosh@gmail.com" class="hover:underline">Josh Shipton</a></p>
  </footer>
</div>
