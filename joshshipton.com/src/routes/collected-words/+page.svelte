<script>
    export let data;
    const { quotes } = data;
</script>

<div>
    {#each quotes as quote}
        <div class="quote">
            <p>{quote.content}</p>
            <p><em>— {quote.author}</em></p>
        </div>
    {/each}
</div>
