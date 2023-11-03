// function to add the nav bar to the top of every file, just cause I ceebs doing it
function addNavBar() {
    console.log("code go brrrrrrr");
    // Create the nav element
    const navElement = document.createElement("nav");
    navElement.setAttribute("id", "top-nav-bar");

    // Create the paragraph element
    const paragraphElement = document.createElement("p");

    // Create the anchor elements and add them to the paragraph
    const homeLink = document.createElement("a");
    homeLink.href = "index.html";
    homeLink.textContent = "Home";

    const reachMeLink = document.createElement("a");
    reachMeLink.href = "reach-me.html";
    reachMeLink.textContent = "Reach me";

    const blogsLink = document.createElement("a");
    blogsLink.href = "quotes.html";
    blogsLink.textContent = "Quote bank";

    // Append the anchor elements to the paragraph element
    paragraphElement.appendChild(homeLink);
    paragraphElement.appendChild(document.createTextNode(" • "));
    paragraphElement.appendChild(reachMeLink);
    paragraphElement.appendChild(document.createTextNode(" • "));
    paragraphElement.appendChild(blogsLink);

    // Append the paragraph element to the nav element
    navElement.appendChild(paragraphElement);

    // Add the nav element as the first child of the body
    document.body.insertBefore(navElement, document.body.firstChild);
}

addNavBar();