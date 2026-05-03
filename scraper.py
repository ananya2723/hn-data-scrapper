import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

titles = soup.find_all("span", class_="titleline")
ranks = soup.find_all("span", class_="rank")

data = []

for i in range(len(titles)):
    link = titles[i].find("a")
    rank = ranks[i].get_text(strip=True) if i < len(ranks) else "N/A"

    if link:
        data.append({
            "rank": rank,
            "title": link.get_text(strip=True),
            "url": link.get("href")
        })

df = pd.DataFrame(data)
df.to_csv("sample_output.csv", index=False)

print("Scraping completed!")