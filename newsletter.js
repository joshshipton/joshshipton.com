let form = document.getElementById('newsletter');
let txt = document.getElementById('newsletter-label');

let given_email = localStorage.getItem('given_email') === 'true';

if(given_email){
    form.remove();
    txt.remove();
} else {
    form.addEventListener("submit", async function(e) {
        e.preventDefault();
        const email = form.elements.email.value;
        console.log(email);
        const response = await fetch('/api/add-email', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email })
        });
    
        if (response.ok) {
            alert("Signed up :)");
            form.reset();
            form.remove();
            txt.remove();
            localStorage.setItem('given_email', 'true');
        } else {
            console.log(response);
            alert("Already Signed up");
        }
    });
}

