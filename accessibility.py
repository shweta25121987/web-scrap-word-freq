

import requests

def check_website_accessibility(url):
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            print(f"The website '{url}' is accessible.")
        elif status_code == 403:
            print(f"The website '{url}' is accessible, but you may be blocked or forbidden from accessing certain content.")
        else:
            print(f"The website '{url}' returned a status code {status_code}, indicating an issue.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while accessing '{url}': {e}")

# Example usage
website_url = "https://google.com"
check_website_accessibility(website_url)