import os
import json
import time
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def scrape_url(url):
    """Scrapes basic on-page SEO metrics from a given URL."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64 AppleWebKit/537.36)'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Calculate approximate word count
        text = soup.get_text(separator=' ', strip=True)
        word_count = len(text.split())
        
        # Calculate Title length
        title = soup.title.string if soup.title else ""
        
        # Get count of H1 and H2 tags
        h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
        h2_tags = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
        
        return {
            "status": "success",
            "word_count": word_count,
            "title_length": len(title),
            "h1_count": len(h1_tags),
            "h2_count": len(h2_tags)
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def collect_seo_data(keywords, analyze_top_n=3):
    """Searches Google for keywords and analyzes the top ranking pages."""
    all_data = []
    
    for keyword in keywords:
        print(f"[*] Analyzing keyword: '{keyword}'...")
        try:
            # 1. Get search rankings (SERP Data via Google Search)
            results = list(search(keyword, num_results=10, sleep_interval=2))
            
            keyword_data = {
                "keyword": keyword,
                "top_rankings_analyzed": []
            }
            
            # 2. Analyze top N results (On-Page SEO tracking)
            for i in range(min(analyze_top_n, len(results))):
                url = results[i]
                rank = i + 1
                
                print(f"    - Scraping rank {rank} URL: {url}")
                on_page_metrics = scrape_url(url)
                
                keyword_data["top_rankings_analyzed"].append({
                    "rank": rank,
                    "url": url,
                    "on_page_metrics": on_page_metrics
                })
                time.sleep(1.5) # Polite delay
            
            all_data.append(keyword_data)
            
        except Exception as e:
            print(f"[!] Error fetching data for '{keyword}': {e}")
            
    return all_data

def generate_insights_local_llm(json_data_path, output_md_path, model_name="gemma2:2b"):
    """Uses a local Ollama LLM to generate insights based on the collected SEO data."""
    try:
        # Read the scraped JSON data
        with open(json_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        prompt = f"""
        You are an expert Technical SEO Consultant. I have collected search engine ranking data for a few keywords.
        The data includes the top ranking URLs, search snippets, word counts, title lengths, and H1/H2 tags.
        
        Data:
        {json.dumps(data, indent=2)}
        
        Please provide an analysis consisting of:
        1. Data Observations: Summarize what type of content is currently ranking for these keywords.
        2. Insightful Trends: Notice any patterns in the top-ranking pages driving their SEO success.
        3. Actionable Recommendations: Give 3 specific recommendations to outrank these competitors.
        
        Format the output as a professional Markdown document. Do not just echo the JSON back. Add analytical value.
        """
        
        print(f"\n[*] Sending data to local Ollama model ({model_name}) for analysis... This might take a minute.")
        
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": model_name,
            "prompt": prompt,
            "stream": False
        })
        
        if response.status_code == 200:
            result_text = response.json().get('response', '')
            with open(output_md_path, 'w', encoding='utf-8') as f:
                f.write(result_text)
            print(f"[*] Success! Local AI Insights report saved to {output_md_path}")
            return True
        else:
            print(f"[!] Ollama API Error: Status {response.status_code} - {response.text}")
            return False

    except Exception as e:
        print(f"[!] AI Generation Failed. Is Ollama running on your machine? Error: {e}")
        return False

if __name__ == "__main__":
    print("=== Automated SEO Data Collector & Local AI Analyst ===")
    
    # Define our target keywords
    target_keywords = ["best open source llms 2024", "how to run ollama locally"]
    
    # Output file paths
    data_file = "seo_data.json"
    report_file = "seo_insights_report.md"
    
    # Step 1: Collect Data
    print("\n>>> STEP 1: Collecting SERP and On-Page SEO Data")
    seo_data = collect_seo_data(target_keywords, analyze_top_n=3)
    
    # Save the raw JSON
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(seo_data, f, indent=4)
    print(f"\n[*] Raw JSON data exported to: {data_file}")
    
    # Step 2: AI Generation with Local Model
    print("\n>>> STEP 2: AI Data Analysis (Local)")
    # Using 'gemma2:2b' because user's machine has limited RAM
    generate_insights_local_llm(data_file, report_file, model_name="gemma2:2b")
    
    print("\n=== Workflow Complete ===")
