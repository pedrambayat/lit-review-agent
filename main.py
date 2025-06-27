from fetch import fetch_papers
from summarizer import summarize_abstract
from writer import save_to_csv

def main():
    topic = input("Enter a topic to search: ")
    papers = fetch_papers(topic, limit=3)
    print(f"Fetched {len(papers)} papers.")
    
    for paper in papers:
        print(f"Summarizing: {paper['title']}")
        paper["summary"] = summarize_abstract(paper["abstract"])

    save_to_csv(papers)
    print("Summaries saved to output/results.csv")

if __name__ == "__main__":
    main()
