import requests
import json

# API endpoint
endpoint = "https://jsonplaceholder.typicode.com/posts"

# STEP 1: Set Custom Headers
headers_get = {
    'User-Agent': 'MyApp/1.0'
}

# STEP 2: Send the GET Request
response_get = requests.get(endpoint, headers=headers_get)

# STEP 3: Inspect the Response
print("\n---  GET RESPONSE  ---")
print(f"Status Code: {response_get.status_code}")
print("\nHEADERS:")
for key, value in response_get.headers.items():
    print(f"{key}: {value}")
print("\nCONTENTS:")
for post in response_get.json():
    for key, value in post.items():
        print(f"{key}: {value}")
    print()

# STEP 4: Prepare Data for POST Request
post_data = {
    'title': 'Title',
    'body': 'Contents.',
    'userId': 1
}

# STEP 5: Send a POST Request
headers_post = {
    'User-Agent': 'MyApp/1.0',
    'Content-Type': 'application/json'
}

response_post = requests.post(endpoint, data=json.dumps(post_data), headers=headers_post)

# STEP 6: Inspect the POST Response
print("---  POST RESPONSE  ---")
print(f"Status Code: {response_post.status_code}")
print("\nCONTENTS:")
for key, value in response_post.json().items():
    print(f"{key}: {value}")
print()