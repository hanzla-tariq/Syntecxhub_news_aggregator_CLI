import requests
import argparse
import json
import pandas as pd

API_KEY = "0e5aff6120d44951b96fc20f52cdead8"  # put your NewsAPI key here

def fetch_news(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("articles", [])

def remove_duplicates(articles):
    titles = set()
    unique = []
    for a in articles:
        if a["title"] not in titles:
            titles.add(a["title"])
            unique.append(a)
    return unique

def save_json(data):
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def export_csv(data):
    df = pd.DataFrame([{
        "title": a["title"],
        "source": a["source"]["name"],
        "date": a["publishedAt"]
    } for a in data])
    df.to_csv("news.csv", index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyword", default="technology")
    parser.add_argument("--export", choices=["csv"])
    args = parser.parse_args()

    articles = fetch_news(args.keyword)

    if not articles:
        print("No news found")
        return

    articles = remove_duplicates(articles)

    save_json(articles)

    if args.export == "csv":
        export_csv(articles)

    print("Done! Total articles:", len(articles))

if __name__ == "__main__":
    main()