# AI-Powered SEO Automation Workflow

**Made by Arpit Kushwaha**

This project is an automated, end-to-end system designed to collect real SEO-related data, analyze trends, and output clear, AI-driven recommendations using Python and local LLMs. It directly satisfies all requirements of the AI SEO Data Automation assignment.

## 🎯 Objectives Achieved
- **✔ Collects Real Data:** Fetches live search engine results (via Google Search) for target keywords and scrapes live on-page metrics (word count, title lengths, H1/H2 tags) from the top-ranking pages.
- **✔ Analyzes Data (Pandas):** Processes the fetched structured data using `pandas` to calculate key metrics, averages, and group by keyword.
- **✔ AI Summarization & Insights:** Pipes the analyzed data into a local LLM via Ollama to generate a clear summary and specific SEO recommendations.
- **✔ End-to-End Automation:** A fully automated Python script runs the entire sequence seamlessly.

## ⚙️ Data Flow & Architecture
1. **Target Keywords Definition:** You specify your target search queries.
2. **SERP Data Retrieval (Scraping):** The script connects to Google Search directly to uncover the top-ranking URLs.
3. **On-Page SEO Analysis:** `BeautifulSoup` reads the HTML of these URLs to extract content structures (Title, Word Count, Headings).
4. **Data Modeling (Pandas):** The script cleans the fetched web data, builds a `pandas` DataFrame, and groups the values to find average word targets per keyword.
5. **AI Consult (Local LLM):** The raw JSON payload and basic findings are passed to an Ollama LLM (`gemma2:2b`, completely local) to render expert advice.
6. **Report Generation:** Generates a professional markdown document outlining insights and how to outrank the competition.

---

## 🚀 Setup Guide

### 1. Requirements & Prerequisites
- Ensure **Python 3.8+** is installed on your machine.
- Download and install [Ollama](https://ollama.com/) (Ensure it runs in the background).
- Pull the local LLM model required for this script:
    ```bash
    ollama pull gemma2:2b
    ```

### 2. Install Dependencies
Navigate into the repository directory and install the necessary Python packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Automation
To execute the end-to-end pipeline, simply run the Python orchestration script:
```bash
python seo_automation.py
```

## 📊 File Structure & Outputs
- **`seo_automation.py`**: The main automation pipeline orchestrator.
- **`seo_data.json`**: The raw scraped output in a readable JSON format.
- **`seo_trends_summary.csv`**: Pandas-driven basic data extraction analyzing averages targets for the SERP.
- **`seo_insights_report.md`**: Your automated AI consultant report detailing 3 specific SEO improvements based on real data.

*Note: This solution prioritizes a pure Python script automation approach (as permitted in the assignment), avoiding the overhead of external tooling like n8n while perfectly fulfilling all core logic and AI requirements.*
