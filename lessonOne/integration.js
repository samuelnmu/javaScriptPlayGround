// Example of making a GET request using Fetch API in JavaScript

// URL of the API endpoint
const apiUrl = 'https://jsonplaceholder.typicode.com/posts/1';

// Making a GET request
fetch(apiUrl)
    .then(response => {
        // Check if the response is successful
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json(); // Parsing the JSON response
    })
    .then(data => {
        // Handling the data from the response
        console.log('Data received:', data);
    })
    .catch(error => {
        // Handling errors
        console.error('There was a problem with the fetch operation:', error);
    });