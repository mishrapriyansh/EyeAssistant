from search import search
from scraper import scrap_data
from parser import extract_data
from config import TRUSTED_DOMAINS,FILE_OUTPUT_DIR
from file_manager import save_data_to_file


def main():
    print("Welcome to the Ophthalmology Web Scraper!")
    user_query = input("Enter the text to be searched: ")
    context_query=f"{user_query} (Ophthalmology OR EYE OR VISION)"
    print("\nSearching DuckDuckGo...")
    results = search(context_query,domains_list=TRUSTED_DOMAINS)
    
    if not results:
        print("No results found. Exiting.")
        return
        
    print(f"Found {len(results)} links. Starting to scrape...\n")
    for site in results:
        html_data = scrap_data(site)
        if html_data:
            extracted_text = extract_data(html_data)
            if extracted_text:
                saved_path = save_data_to_file(site['href'], extracted_text, topic_name=user_query, base_dir=FILE_OUTPUT_DIR)
            else:
                print(f"\nWARNING - Page loaded, but no text found on {site['href']}")

    print("Job Complete!")
if __name__ == "__main__":
    main()