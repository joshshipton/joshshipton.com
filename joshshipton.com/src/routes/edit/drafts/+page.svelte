<!-- <script>
  export let data;
  const drafts = data;
  
</script>

<div class="flex flex-col h-screen">
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
          {#each drafts as draft}
          <tbody class="[&amp;_tr:last-child]:border-0">
            <tr
              class="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted"
            >
              <td
                class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0 font-medium"
                >{draft.title}</td
              >
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0"
                >{draft.date_created}</td
              >
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
                {#if draft.content_peek}
                {draft.peek}
                {:else}
                <p>draft peek goes here</p>
                {/if}
              </td>
              <td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
                <a href="edit-post/{draft.id}">
                <button
                  class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 rounded-md px-3"
                  >
                  Edit
                </button>
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</div> -->
