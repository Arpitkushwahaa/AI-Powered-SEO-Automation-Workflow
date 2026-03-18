# AI-Powered SEO Automation Agent

This is a free, local automation pipeline that gathers real SEO metrics and generates actionable insights using your local **Ollama** LLMs. 

## What It Does
1. **SERP Data Collection**: Connects to the DuckDuckGo search engine to find the top URLs for a given list of keywords.
2. **On-Page SEO Scraper**: Scrapes **Word Count, Title Lengths, H1, and H2 elements** of the ranking pages.
3. **Data Storage**: Consolidates the findings and saves them as `seo_data.json`.
4. **Local AI Analysis**: Sends the JSON data into your local **Ollama** model (e.g., `mistral:latest` or `gemma2:2b`) via its local API (`localhost:11434`), and outputs a markdown report in `seo_insights_report.md`.

---

## 🚀 Setup Guide

### 1. Requirements
Ensure you have **Python 3.8+** installed. Also ensure you have **Ollama** running in the background.

```bash
pip install -r requirements.txt
```

### 2. Running the Automation
Just run the script! It requires **NO** API keys and costs **$0**.

```bash
python seo_automation.py
```

## Generated Outputs
Once executed, it produces:
- **`seo_data.json`**: The scraped raw data.
- **`seo_insights_report.md`**: Your automated local AI consultant report.
