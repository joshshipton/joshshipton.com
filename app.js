let postData = [
    {
      "title": "Hello world",
      "link": "https://joshshipton.com/hello-world",
      "date": "11/10/2023",
      "peek": "I've finally decided to go ahead and start a blog. Blog is probably pushing it, to be honest. You can think of this as a collective home for all of my ramblings that won't get me canceled.",
      "tags": ["first-post, hello world"],
    }
  ];


// function to make and fill the recent posts part of the "blog"
function getRecentPosts(){
  for (let i = 0; i < postData.length; i++) {
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

getRecentPosts();