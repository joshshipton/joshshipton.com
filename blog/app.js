let postData = [
    {
      "title": "Hello_world",
      "date": "11/10/2023",
      "peek": "I've finally decided to go ahead and start a blog. Blog is probably pushing it, to be honest. You can think of this as a collective home for all of my ramblings that won't get me canceled."
    }
  ];
  
  for (let i = 0; i < postData.length; i++) {
    let content = postData[i];
  
    // Create elements for title, date, and peek
    let title = document.createElement("p");
    title.textContent = content.title;
    title.setAttribute("id", "post-title");

  
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
    posts.setAttribute("id", "a-single-post");
    posts.appendChild(post);
  }
  