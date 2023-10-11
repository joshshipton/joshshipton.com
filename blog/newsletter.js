// code to send new posts to every one that signs up
// so it first needs to save the emails somewhere 
//  at this point I think its impossible without either exposing an api key 

// if i could somehow build my own server that checks emails that would be dobable tho....

form = document.getElementById('newsletter');

form.addEventListener("submit", function(e){
    e.preventDefault();

    const email = form.elements.email.value;
    console.log("Email submitted it:", email);
    alert("signed up :)");
    const emailInput = form.elements.email;
    emailInput.value = '';

})