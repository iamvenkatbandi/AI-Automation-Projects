# 🤖 AI Google Sheets Automation Bot

An AI-powered automation tool that reads data from Google Sheets, generates intelligent outputs like summaries, tags, and marketing captions using LLM APIs, and writes the results back automatically.

---

## 🚀 Features

* 📊 Read data from Google Sheets
* 🤖 Generate AI-powered:

  * Summaries
  * Tags
  * Marketing Captions
* 🔄 Automatically update results back to Google Sheets
* 🖥️ CLI-based interface for easy interaction
* ✅ Status tracking for processed rows

---

## 🧠 Tech Stack

* Python
* Google Sheets API (gspread, oauth2client)
* LLM API (OpenRouter / Llama 3)
* Requests
* Python Dotenv

---

## 📂 Project Structure

ai-sheets-bot/
│── app.py          # CLI interface
│── main.py         # Automation script
│── ai.py           # AI integration
│── sheets.py       # Google Sheets connection
│── requirements.txt
│── .gitignore

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/your-username/ai-sheets-bot.git
cd ai-sheets-bot

---

### 2️⃣ Install Dependencies

pip install -r requirements.txt

---

### 3️⃣ Setup Environment Variables

Create a `.env` file:

OPENROUTER_API_KEY=your_api_key_here

---

### 4️⃣ Setup Google Sheets API

* Go to Google Cloud Console
* Create a new project
* Enable:

  * Google Sheets API
  * Google Drive API
* Create Service Account
* Download `credentials.json`
* Share your Google Sheet with service account email

---

## 🔐 Important Note

This project requires API keys and credentials which are not included for security reasons.

To run this project:

* Add your OpenRouter API key in `.env`
* Add your Gmail API `credentials.json` from Google Cloud Console

---

## 📊 Google Sheet Format

| Input Text | Summary | Tags | Caption | Status |

---

## ▶️ Usage

### Run CLI App

python app.py

---

### Run Automation Script

python main.py

---

## 💡 Example Output

| Input Text                | Summary                   | Tags           | Caption                   | Status |
| ------------------------- | ------------------------- | -------------- | ------------------------- | ------ |
| Running shoes for comfort | Lightweight running shoes | shoes, fitness | Run smarter and faster 🚀 | Done   |

---

## 🔐 Security Note

* `.env` and `credentials.json` are excluded using `.gitignore`
* Never expose API keys publicly

---

## 📌 Future Improvements

* 🌐 Web UI (Streamlit / FastAPI)
* ⏱️ Scheduled automation (cron jobs)
* 📈 Analytics dashboard
* 🔑 Authentication system

---

## 💼 Resume Description

Built an AI-powered Google Sheets automation tool using Python and LLM APIs to generate summaries, tags, and marketing content, improving workflow efficiency and automating repetitive tasks.

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/iamvenkatbandi

---

## ⭐ If you found this useful, consider giving a star!

