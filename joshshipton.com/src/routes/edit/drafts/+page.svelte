<script>
  export let data;
</script>

<div class="flex flex-col h-screen">
  <header
    class="flex h-[60px] items-center gap-4 border-b bg-gray-100/40 px-6 dark:bg-gray-800/40"
  >
    <a class="lg:hidden" href="#">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="h-6 w-6"
      >
        <path d="M3 9h18v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9Z"></path>
        <path d="m3 9 2.45-4.9A2 2 0 0 1 7.24 3h9.52a2 2 0 0 1 1.8 1.1L21 9"
        ></path>
        <path d="M12 3v6"></path>
      </svg>
      <span class="sr-only">Home</span>
    </a>
    <div class="w-full flex-1">
      <form>
        <div class="relative">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="absolute left-2.5 top-2.5 h-4 w-4 text-gray-500 dark:text-gray-400"
          >
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.3-4.3"></path>
          </svg>
          <input
            class="flex h-10 rounded-md border border-input px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 w-full bg-white shadow-none appearance-none pl-8 md:w-2/3 lg:w-1/3 dark:bg-gray-950"
            placeholder="Search drafts..."
            type="search"
          />
        </div>
      </form>
    </div>
    <button
      class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:bg-accent hover:text-accent-foreground rounded-full border border-gray-200 w-8 h-8 dark:border-gray-800"
      type="button"
      id="radix-:r10:"
      aria-haspopup="menu"
      aria-expanded="false"
      data-state="closed"
    >
      <img
        src="/placeholder.svg"
        width="32"
        height="32"
        class="rounded-full"
        alt="Avatar"
        style="aspect-ratio: 32 / 32; object-fit: cover;"
      />
      <span class="sr-only">Toggle user menu</span>
    </button>
  </header>
  <main class="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-6">
    <div class="flex items-center">
      <h1 class="font-semibold text-lg md:text-2xl">Drafts</h1>
    </div>
    <div class="border shadow-sm rounded-lg">
      <div class="relative w-full overflow-auto">
        <table class="w-full caption-bottom text-sm">
          <thead class="[&amp;_tr]:border-b">
            <tr
              class="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted"
            >
              <th
                class="h-12 px-4 text-left align-middle font-medium text-muted-foreground [&amp;:has([role=checkbox])]:pr-0 w-[80px]"
              >
                Title
              </th>
              <th
                class="h-12 px-4 text-left align-middle font-medium text-muted-foreground [&amp;:has([role=checkbox])]:pr-0 max-w-[150px]"
              >
                Date
              </th>
              <th
                class="h-12 px-4 text-left align-middle font-medium text-muted-foreground [&amp;:has([role=checkbox])]:pr-0"
              >
                Preview
              </th>
              <th
                class="h-12 px-4 text-left align-middle font-medium text-muted-foreground [&amp;:has([role=checkbox])]:pr-0"
              >
                Actions
              </th>
            </tr>
          </thead>
          <tbody class="[&amp;_tr:last-child]:border-0">
            <tr
              class="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted"
            >
              <td
                class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0 font-medium"
                >Post Title</td
              >
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0"
                >January 1, 2024</td
              >
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
                This is a preview of the post content...
              </td>
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
                <button
                  class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 rounded-md px-3"
                >
                  Edit
                </button>
              </td>
            </tr>
            <tr
              class="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted"
            >
              <td
                class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0 font-medium"
                >Another Post Title</td
              >
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0"
                >December 31, 2023</td
              >
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
                This is another preview of the post content...
              </td>
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
                <button
                  class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 rounded-md px-3"
                >
                  Edit
                </button>
              </td>
            </tr>
            <tr
              class="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted"
            >
              <td
                class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0 font-medium"
                >Yet Another Post Title</td
              >
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0"
                >December 30, 2023</td
              >
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
                This is yet another preview of the post content...
              </td>
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
                <button
                  class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 rounded-md px-3"
                >
                  Edit
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</div>
