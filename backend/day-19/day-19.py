import requests

endpoint = "https://api.spacexdata.com/v5/launches/latest"

headers = {
    'User-Agent': 'MyApp/1.0'
}

response = requests.get(endpoint, headers=headers)

if response.status_code == 200:
    data = response.json()

    name = data["name"]
    date_utc = data["date_utc"]
    success = data["success"]
    patch_image_url = data["links"]["patch"]["small"]
    webcast_url = data["links"]["webcast"]

    print("\n-- Latest SpaceX Launch Information --")
    print(f"\nName: {name}")
    print(f"Date (UTC): {date_utc}")
    print(f"Success: {'Yes' if success else 'No'}")
    print("\nDETAILS:")
    print(f"Patch Image: {patch_image_url}")
    print(f"Webcast URL: {webcast_url}\n")
else:
    print(f"\nRequest failed with status code: {response.status_code}\n")