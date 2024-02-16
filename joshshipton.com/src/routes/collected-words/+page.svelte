<script>
    export let data;
    const { quotes } = data;
</script>

<div>
    {#each quotes as quote}
        <div class="quote">
            <p>{quote.content}</p>
            {#if quote.source}
            <a href={quote.source}>
            <p><em>— {quote.author}</em></p>
            </a>
           {:else}
            <p><em>— {quote.author}</em></p>
            {/if}
        </div>
    {/each}
</div>
