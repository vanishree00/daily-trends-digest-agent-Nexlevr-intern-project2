# Daily Trends Digest Agent

## Project Overview

The Daily Trends Digest Agent is an AI-powered technology news summarization system built using Python, RSS feeds, and Google's Gemini API.

The agent collects the latest technology news from five different RSS sources, analyses the collected articles using Gemini AI, and generates a daily digest containing five important technology trends and creative social media post ideas for a technology brand.

The generated digest is automatically saved as a Markdown file.

## Features

- Collects technology news from five RSS sources.
- Extracts article titles, summaries, publication dates, and source links.
- Uses Google Gemini AI to analyse and summarize news.
- Identifies five important technology trends.
- Generates three creative social media post ideas.
- Includes original news source links.
- Saves the generated digest automatically in Markdown format.
- Supports daily execution using Windows Task Scheduler.

## Technology Stack

- Python
- Google Gemini API
- Feedparser
- Python-dotenv
- RSS Feeds
- Windows Task Scheduler
- Markdown

## News Sources

The project collects news from:

1. TechCrunch
2. The Verge
3. Ars Technica
4. MIT Technology Review
5. Wired

## Project Structure

```text
daily-trends-digest-agent/
│
├── main.py
├── rss_feeds.py
├── ai_summarizer.py
├── requirements.txt
├── .env
├── .gitignore
│
└── output/
    └── daily_digest.md
```

## How It Works

1. The RSS collector fetches the latest articles from five technology news sources.
2. Article information is extracted using the Feedparser library.
3. The collected news is passed to the Gemini AI model.
4. Gemini analyses the articles and generates five important technology trends.
5. The AI also suggests three social media post ideas for a technology brand.
6. The final digest is displayed in the terminal and saved as a Markdown file.
7. Windows Task Scheduler can execute the program automatically every day.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd daily-trends-digest-agent
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Gemini API key

Create a `.env` file in the project folder.

Add:

```env
GEMINI_API_KEY=your_gemini_api_key
```



## Run the Project

Execute the following command:

```bash
python main.py
```

The program will collect news, generate an AI-powered digest, display the result, and save it inside the output folder.

## Output

The generated report is saved at:

```text
output/daily_digest.md
```

The digest includes:

- Five important technology trends.
- Three creative social media post ideas.
- Relevant source links.

## Automation

Windows Task Scheduler is used to schedule the Python program to run automatically every day at 8:00 AM.

This allows the agent to generate updated technology news digests without manually executing the Python script.

## Security

- API credentials are stored in a local `.env` file.
- The `.env` file is excluded from Git tracking.
- Virtual environment files are excluded from the repository.

## Learning Outcomes

Through this project, I gained practical experience in:

- Working with RSS feeds.
- Collecting and processing real-world news data.
- Integrating the Gemini API with Python.
- Building an AI-powered summarization workflow.
- Using environment variables for API key management.
- Automating Python scripts using Windows Task Scheduler.

## Author

Vanishree 

Agentic AI Developer Intern