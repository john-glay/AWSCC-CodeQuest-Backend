import requests

endpoint = "https://jsonplaceholder.typicode.com/"

response = requests.get(endpoint)

if response.status_code == 200:
    print("\nRequest successful.\n")
else:
    print("\nRequest failed.\n")
