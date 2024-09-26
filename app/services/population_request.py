import requests

def fetch_population_data():
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Request failed with status code: {response.status_code}"

