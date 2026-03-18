# AI-Powered SEO Automation Workflow

**Made by Arpit Kushwaha**  
*A complete, end-to-end automation system that collects real SEO data, analyzes it, and generates AI-driven recommendations.*

---

## 📖 Project Overview
This project is built to autonomously analyze search engine results for target keywords and provide actionable SEO advice. Instead of relying on manual tools, it uses a pipeline constructed with **n8n (for orchestration)**, **Python & Pandas (for data collection and analysis)**, and local AI via **Ollama (for generating insights)**.

This repository directly fulfills all the requirements of the AI SEO Data Automation assignment.

---

## 🛠️ How It Works (Project Q&A)
*If you are evaluating this project, here are the answers to how the system functions under the hood:*

### 1. How is this system orchestrated? (Automation)
The workflow is orchestrated using **n8n**. A provided `n8n_workflow.json` acts as the central conductor. It uses a **Schedule Trigger** to run entirely hands-off at regular intervals. When triggered, n8n executes the primary Python script and then reads the newly generated insight reports back into the system.

### 2. How is real SEO data collected? (Data Fetching)
The system does **not** use dummy data. When executed, the Python script:
1. Performs a live Google Search using the `googlesearch-python` library for specific target keywords.
2. Navigates to the top-ranking URLs.
3. Uses `BeautifulSoup` to scrape **live on-page metrics** (e.g., HTML title length, approximate word count, and H1/H2 heading counts).
4. Saves this raw nested metric data into `seo_data.json`.

### 3. How is the data analyzed? (Pandas Processing)
Once the data is fetched, the script uses the **Pandas** library. It flattens the scraped JSON data into a structured DataFrame. Then, it groups the data by keyword to calculate the **mean (average) word count and heading frequencies** of top-ranking pages. These aggregated statistics represent the "target metrics" needed to rank. Finally, Pandas exports these trends to `seo_trends_summary.csv`.

### 4. How are AI insights generated? (LLM Integration)
Instead of relying on paid APIs (like OpenAI), this project leverages **Ollama** to run models purely locally. 
- It formats the extracted Pandas metrics and raw JSON into a prompt.
- Sends a POST request to the local Ollama API server running the `gemma2:2b` model.
- Instructs the AI act as an SEO Consultant.
- Outputs a cleanly formatted Markdown report (`seo_insights_report.md`) detailing three specific, data-backed recommendations to outrank competitors.

---

## 🎯 Assignment Objectives Met
| Criteria | How It Was Achieved in This Project |
| :--- | :--- |
| **Real Use Case** | Gathers live ranking data directly from Google Search SERPs and parses real HTML. |
| **Automation** | Handled natively by importing the provided **n8n workflow**. |
| **Data Analysis** | Uses **Pandas** to compute mathematical averages of opponent pages. |
| **AI Summary** | Autonomous local LLM integration generating realistic summary reports. |

---

## 🚀 Setup & Execution Guide

### Step 1: Core Prerequisites
- **Python 3.8+**: Ensure Python is installed on your system.
- **Ollama**: Download and install [Ollama](https://ollama.com/) (Ensure it runs in the background).
- **n8n**: Install n8n globally via npm (`npm install -g n8n`).

### Step 2: Prepare the LLM
Open your terminal and pull the local LLM model used by the script:
```bash
ollama pull gemma2:2b
```

### Step 3: Install Python Dependencies
Navigate into this repository directory and install the necessary Python packages:
```bash
pip install -r requirements.txt
```
*(This installs `requests`, `beautifulsoup4`, `googlesearch-python`, and `pandas`)*

### Step 4: Import and Run the n8n Workflow
1. Start your local n8n server by typing `n8n` in your terminal.
2. Open the n8n dashboard (usually `http://localhost:5678`).
3. Click **Add Workflow** > **Import from File**.
4. Select `n8n_workflow.json` from this repository.
5. Click **Execute Workflow** to test the system manually, or leave it active to run on its defined schedule!

*(Alternatively, you can manually test just the script by running `python seo_automation.py` in your terminal).*

---

## 📊 Repository File Structure
- `n8n_workflow.json`: The main n8n orchestrator that handles scheduling and triggers.
- `seo_automation.py`: The core engine handling web scraping, pandas math, and LLM requests.
- `.env.example`: Template for environment variables (if API scaling is needed later).
- `requirements.txt`: Project dependencies list.
- **Generated Outputs** (Created automatically upon execution):
  - `seo_data.json`: The complete log of raw site metrics.
  - `seo_trends_summary.csv`: The Pandas-analyzed trend data.
  - `seo_insights_report.md`: The final readable advice document from the AI.
