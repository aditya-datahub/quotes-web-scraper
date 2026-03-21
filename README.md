# 📌 Quotes Web Scraper

> 🚀 An automated web scraping project that extracts quotes, authors, and tags from a multi-page website using Python.

---

## 📖 Project Overview
This project collects data from a website and converts unstructured HTML into a clean, structured dataset.  
It also simulates a **real-world data pipeline** by automating the scraping process.

---

## 🛠️ Tech Stack
**Python • BeautifulSoup • Pandas**

---

## 🚀 Features
✨ Multi-page web scraping  
✨ Extracts quotes, authors, and tags  
✨ Stores data in CSV format  
✨ Includes error handling  
✨ Adds timestamp for each record  
✨ Maintains execution logs  

---

## 🤖 Automation
This project supports automation using system schedulers (e.g., Task Scheduler or Cron Jobs).

- Runs automatically at scheduled intervals  
- Updates dataset without manual execution  
- Logs each run in `run_log.txt`  

---

## 📊 Output
📁 `quotes_data.csv` — Contains:
- Quote text  
- Author name  
- Tags  
- Scraped timestamp  

📁 `run_log.txt` — Tracks each automated run  

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

2️⃣ Run the script
```
python quotes_scraper.py
```
