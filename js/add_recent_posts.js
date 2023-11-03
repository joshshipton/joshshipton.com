function fetchPosts() {
    fetch('data/posts.json')
        .then(response => response.json())
        .then(data => displayPosts(data))
        .catch(error => console.error('Error fetching posts:', error));
}

function displayPosts(postData) {
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

fetchPosts();