// Fetch quotes from JSON
fetch('data/quotes.json')
    .then(response => response.json())
    .then(quotes => {
        // Always display the first quote
        let output = `<p>${quotes[0].quote} ― <i>${quotes[0].author}</i></p>`;

        // Remove the first quote and shuffle the remaining quotes
        quotes.shift();
        shuffleArray(quotes);

        // Append the shuffled quotes to the output
        quotes.forEach(quoteObj => {
            output += `<p>${quoteObj.quote} ― <i>${quoteObj.author}</p></i>`;
        });

        document.getElementById('quotes-list').innerHTML = output;
    })
    .catch(error => console.error('Error fetching quotes:', error));

// Utility function to shuffle an array
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}