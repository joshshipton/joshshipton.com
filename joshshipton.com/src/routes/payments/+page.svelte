<script>
  import { onMount } from 'svelte';

  // Initialize copy functions after component mounts (client-side only)
  onMount(() => {
    const createCopyFunction = (elementId) => {
      const element = document.getElementById(elementId);
      if (!element) return;

      element.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(element.textContent);
          const originalText = element.textContent;
          element.textContent = 'Copied!';
          element.classList.add('copy-success');

          setTimeout(() => {
            element.textContent = originalText;
            element.classList.remove('copy-success');
          }, 1000);
        } catch (err) {
          console.error('Failed to copy:', err);
        }
      });
    };
    ['aus-bsb', 'aus-acc', 'int-bsb', 'int-acc'].forEach(createCopyFunction);
  });
</script>

<div>
  <h2> if you want/need to send me money for whatever reason </h2>

  <h3> bank details (australian) </h3>
  <p>bsb - <span class="copy-text" id="aus-bsb">066209</span></p>
  <p>account number - <span class="copy-text" id="aus-acc">10171 1308</span></p>

  <h3> bank details (international) </h3>
  <p>bsb - <span class="copy-text" id="int-bsb">774001</span></p>
  <p>account number - <span class="copy-text" id="int-acc">224298563</span></p>
</div>

<style>

  .copy-text {
    display: inline-block;
    padding: 5px 10px;
    background-color: #f5f5f5;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s;
    user-select: none;
  }

  .copy-text:hover {
    background-color: #e0e0e0;
  }

  :global(.copy-success) {
    background-color: #d4edda !important;
  }
</style>
