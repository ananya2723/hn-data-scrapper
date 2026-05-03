# Hacker News Scraper API

A backend system that scrapes and serves real-time data from Hacker News using FastAPI.

## Features
- Scrapes live news data from web
- Extracts rank, title, and URL
- Provides REST API endpoints
- Implements caching for efficiency

## API Endpoints

- `GET /news` → Get latest news
- `GET /news?limit=5` → Get limited results
- `GET /news/{rank}` → Get specific article

## Tech Stack
- Python
- FastAPI
- BeautifulSoup
- Requests

## How to Run

```bash
pip install -r requirements.txt
uvicorn api:app --reload
