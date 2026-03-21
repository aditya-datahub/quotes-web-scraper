# 📌 Quotes Web Scraper

> 🚀 A web scraping project that extracts quotes, authors, and tags from a multi-page website using Python.

---

## 📖 Project Overview
This project collects data from a website and converts unstructured HTML into a clean, structured dataset.  
It also tracks when the data is scraped using timestamps and maintains execution logs.

---

## 🛠️ Tech Stack
**Python • BeautifulSoup • Pandas**

---

## 🚀 Features
- 🔹 Multi-page web scraping  
- 🔹 Extracts quotes, authors, and tags  
- 🔹 Stores data in CSV format  
- 🔹 Includes error handling  
- 🔹 Adds timestamp for each record  
- 🔹 Maintains execution logs  

---

## ⏱️ Logging & Timestamp
This project records the time at which data is scraped and maintains a log of each execution.

- 🕒 Adds a timestamp (`Scraped_At`) to each record  
- 📝 Stores execution logs in `run_log.txt`  
- 📊 Helps track when the data was collected  

---

## 📊 Output
- 📁 `quotes_data.csv` → Contains scraped data (quotes, authors, tags, timestamp)  
- 📁 `run_log.txt` → Tracks script execution history  

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Run the script
```
python quotes_scraper.py
```
