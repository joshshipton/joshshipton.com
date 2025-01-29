<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Footer Example</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .content {
            flex: 1;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        .footer {
            padding: 10px 0;
            text-align: center;
            font-size: 12px;
            color: #000;
        }
        .footer a {
            color: #000;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .image-container {
            text-align: center;
            margin: 20px 0;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>Sample Travel Review</h1>
        <div class="image-container">
            <img src="/api/placeholder/800/400" alt="Travel destination" />
        </div>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>

        <h2>Destination Highlights</h2>
        <div class="image-container">
            <img src="/api/placeholder/800/400" alt="Destination highlights" />
        </div>
        <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    <div class="footer">
        <p>Website by <a href="mailto:shiptonjosh@gmail.com">Josh Shipton</a></p>
    </div>
</body>
</html>
