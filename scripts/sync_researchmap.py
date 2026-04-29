import requests
import json
from datetime import datetime

RESEARCHMAP_ID = "ichio"

def fetch_works():
    url = f"https://api.researchmap.jp/{RESEARCHMAP_ID}/presentations"
    response = requests.get(url, headers={"Accept": "application/json"})
    return response.json()

def fetch_papers():
    url = f"https://api.researchmap.jp/{RESEARCHMAP_ID}/published_papers"
    response = requests.get(url, headers={"Accept": "application/json"})
    return response.json()

def main():
    print("Fetching from researchmap...")
    works = fetch_works()
    papers = fetch_papers()
    
    print(f"\n=== Presentations ({len(works.get('items', []))} entries) ===")
    for item in works.get("items", []):
        title = item.get("presentation_title", {}).get("en") or item.get("presentation_title", {}).get("ja", "")
        date = item.get("publication_date", "")
        venue = item.get("event_name", {}).get("en") or item.get("event_name", {}).get("ja", "")
        print(f"  [{date}] {title} — {venue}")

    print(f"\n=== Papers ({len(papers.get('items', []))} entries) ===")
    for item in papers.get("items", []):
        title = item.get("paper_title", {}).get("en") or item.get("paper_title", {}).get("ja", "")
        date = item.get("publication_date", "")
        journal = item.get("journal_title", {}).get("en") or item.get("journal_title", {}).get("ja", "")
        print(f"  [{date}] {title} — {journal}")

    print("\nReview the above, then manually update your .qmd files.")
    print(f"Last checked: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

if __name__ == "__main__":
    main()