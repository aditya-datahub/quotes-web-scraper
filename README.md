# 📌 Quotes Web Scraper

> 🚀 An automated web scraping project that extracts quotes, authors, and tags from a multi-page website using Python and runs on cloud using GitHub Actions.

---

## 📖 Project Overview
This project extracts data from a website and transforms unstructured HTML into a clean, structured dataset.  
The scraper is automated using GitHub Actions, allowing it to run on cloud without manual execution.

---

## 🛠️ Tech Stack
**Python • BeautifulSoup • Pandas • GitHub Actions**

---

## 🚀 Features
- 🔹 Multi-page web scraping  
- 🔹 Extracts quotes, authors, and tags  
- 🔹 Stores data in CSV format  
- 🔹 Includes error handling  
- 🔹 Adds timestamp for each record  
- 🔹 Maintains execution logs  
- 🔹 Automated execution using GitHub Actions 🤖  

---

## 🤖 Automation (GitHub Actions)
This project uses GitHub Actions to automate scraping.

- ⚡ Runs scraper on cloud (no local machine required)  
- ▶️ Can be triggered manually from Actions tab  
- 🔁 Can be extended to run on schedule (daily/weekly)  
- 📊 Ensures consistent and repeatable data collection  

---

## ⏱️ Logging & Timestamp
This project records when the data is scraped and maintains execution logs.

- 🕒 Adds a timestamp (`Scraped_At`) to each record  
- 📝 Stores execution logs in `run_log.txt`  
- 📊 Helps track data freshness and scraping history  

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

---

## ▶️ Run via GitHub Actions (Recommended)
1. Go to **Actions** tab  
2. Select **Run Quotes Scraper** workflow  
3. Click **Run workflow**  

👉 Script will execute on cloud and scrape data automatically  

---

## 💡 Future Improvements
- 🔸 Schedule automated runs (daily scraping)  
- 🔸 Store data in database (instead of CSV)  
- 🔸 Build dashboard for data analysis (Power BI / Tableau)  

---

## 💯 What this project demonstrates
- Web scraping fundamentals  
- Data cleaning & structuring  
- Automation using CI/CD tools  
- Real-world data pipeline thinking  
