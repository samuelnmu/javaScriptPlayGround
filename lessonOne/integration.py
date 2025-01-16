# Example of making a GET request using Requests library in Python

import requests

# URL of the API endpoint
api_url = 'https://jsonplaceholder.typicode.com/posts/1'

try:
    # Making a GET request
    response = requests.get(api_url)
    # Check if the response is successful
    response.raise_for_status()
    # Parsing the JSON response
    data = response.json()
    # Handling the data from the response
    print('Data received:', data)
except requests.exceptions.HTTPError as http_err:
    # Handling HTTP errors
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    # Handling other errors
    print(f'Other error occurred: {err}')