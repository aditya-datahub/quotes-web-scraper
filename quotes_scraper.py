import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_quotes():
    base_url = "http://quotes.toscrape.com/page/{}/"
    all_data = []

    for page in range(1, 6):
        url = base_url.format(page)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except:
            print(f"Error on page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            text = q.find("span", class_="text").text.strip()
            author = q.find("small", class_="author").text.strip()
            tags = [tag.text for tag in q.find_all("a", class_="tag")]

            all_data.append({
                "Quote": text,
                "Author": author,
                "Tags": ", ".join(tags)
            })

        print(f"Page {page} scraped ✅")
        time.sleep(1)

    df = pd.DataFrame(all_data)
    df.to_csv("quotes_data.csv", index=False)

    print("All data saved successfully 🎉")


if __name__ == "__main__":
    scrape_quotes()