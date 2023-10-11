

// get rid of .html
// apparently this can fuck up the SEO but idgaf
if (window.location.pathname.endsWith('.html')) {
    window.location.pathname = window.location.pathname.slice(0, -5);
  }