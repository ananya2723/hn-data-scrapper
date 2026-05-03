from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

def scrape_hn():
    url = "https://news.ycombinator.com"
    headers = {"User-Agent": "Mozilla/5.0"}

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

    return data


@app.get("/")
def home():
    return {"message": "HN Scraper API is running"}


@app.get("/news")
def get_news():
    data = scrape_hn()
    return {"articles": data[:10]}


@app.get("/news/{rank}")
def get_by_rank(rank: str):
    data = scrape_hn()

    for item in data:
        if item["rank"].replace(".", "") == rank:
            return item

    return {"error": "Not found"}