let postData = [{
        "title": "Hello world",
        "link": "/hello-world.html",
        "date": "11/10/2023",
        "peek": "I've finally decided to go ahead and start a blog. Blog is probably pushing it, to be honest. You can think of this as a collective home for all of my ramblings that won't get me canceled.",
        "tags": ["first-post, hello world"],
    }, { 'title': "Mabye being bored isn't so bad", 'link': '/boredom.html', 'date': '21/10/2023', 'peek': "when you’re doing nothing a lot more things suddenly become more fun than what you’re doing right now." },
    { 'title': 'If you don’t like something. maybe you just haven’t done it enough', 'link': '/enjoying-things.html', 'date': '25/10/2023', 'peek': 'Life hack I’ve realized lately. Pretty much anythi' }, { 'title': 'Why you should outsource your opinions', 'link': '/opinions.html', 'date': '3/11/2023', 'peek': 'Epistemology is fucked. Knowing things, and knowing that you know things is' }
];


// function to make and fill the recent posts part of the "blog"
function getRecentPosts() {
    for (let i = postData.length - 1; i >= 0; i--) {
        let content = postData[i];

        // Create elements for title (as an <a> tag), date, and peek
        let title = document.createElement("a");
        title.textContent = content.title;
        title.setAttribute("id", "post-title");
        title.setAttribute("href", content.link); // Set the href attribute

        let date = document.createElement("p");
        date.textContent = content.date;
        date.setAttribute("id", "post-date");

        let peek = document.createElement("p");
        peek.textContent = content.peek.substring(0, 100) + "......";
        peek.setAttribute("id", "post-peek");

        let post = document.createElement('div');

        // Append the elements to the document (e.g., to a container div)
        post.appendChild(title);
        post.appendChild(date);
        post.appendChild(peek);

        let posts = document.getElementById('posts');
        post.setAttribute("class", "a-single-post"); // Use "class" to apply styling
        posts.appendChild(post);
    }
}

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
getRecentPosts();