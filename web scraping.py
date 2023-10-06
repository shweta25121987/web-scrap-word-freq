import requests
from bs4 import BeautifulSoup


def get_latest_python_articles():
    url = "https://www.python.org/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        latest_articles = []

        for article in soup.select(".blog-widget li"):
            title = article.a.text.strip()
            latest_articles.append(title)

        return latest_articles
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []


if __name__ == "__main__":
    python_articles = get_latest_python_articles()

    if python_articles:
        print("Latest articles in the Python section:")
        for index, article in enumerate(python_articles, 1):
            print(f"{index}. {article}")
    else:
        print("No articles found.")
        
        #with open('outfile.txt', 'w') as outfile:
            # print(outfile, 'Data collected on:', input['header']['timestamp'].date())