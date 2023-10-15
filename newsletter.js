let form = document.getElementById('newsletter');

form.addEventListener("submit", async function(e) {
  e.preventDefault();
  const email = form.elements.email.value;
  
  const response = await fetch('/api/add-email', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });
  
  if (response.ok) {
    alert("Signed up :)");
    form.reset();
    form.remove();
  } else {
    alert("Failed to sign up.");
  }
});
