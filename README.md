# 📈 CodeAlpha_Stock-Portfolio-Tracker
A Python-based Stock Portfolio Tracker developed using **Python and Flask** as part of the **CodeAlpha Python Programming Internship**.
This web application allows users to enter the quantity of shares they own, calculate individual stock values, and view their total portfolio investment value. It also provides downloadable portfolio reports in CSV and TXT formats.

## 🚀 Features
- 📊 **Stock Portfolio Management** – Enter quantities of different stocks.
- 💰 **Automatic Calculation** – Calculates investment value using quantity × share price.
- 📈 **Total Portfolio Value** – Displays the combined investment value.
- 📋 **Holdings Breakdown** – Shows stock name, quantity, price per share, and investment value.
- 📥 **Download Reports** – Export portfolio details in CSV and TXT formats.
- ⚠️ **Input Validation** – Prevents invalid and negative share quantities.
- 🎨 **User-Friendly Interface** – Clean and responsive web design.

## 🛠️ Technologies Used
- Python
- Flask Framework
- HTML
- CSS
- CSV File Handling
- Python Dictionaries

## 📂 Project Structure

```text
Stock_Portfolio_Tracker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── portfolio.csv
│   └── portfolio_summary.txt
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    └── result.html
```

## ⚙️ Installation and Setup
**Step 1: Clone the Repository**
```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

**Step 2: Navigate to the Project Folder**
```bash
cd Stock_Portfolio_Tracker
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Run the Application**
```bash
python app.py
```

**Step 5: Open in Browser**
```text
http://127.0.0.1:5000
```

## 🧮 How It Works
1. Open the Stock Portfolio Tracker website.
2. Enter the number of shares owned for the available stocks.
3. Click on Calculate My Portfolio.
4. The application calculates the investment value of each stock.
5. View the total investment and holdings breakdown.
6. Download the portfolio report in CSV or TXT format.

## 📌 Sample Calculation
| Stock | Quantity | Sample Price | Investment |
|---|---:|---:|---:|
| AAPL | 5 | $180 | $900 |
| TSLA | 2 | $250 | $500 |
| MSFT | 3 | $420 | $1,260 |

**Total Portfolio Value: $2,660**

## 📚 Learning Outcomes
Through this project, I gained practical experience in:
- Python programming and functions.
- Dictionaries and data structures.
- File handling using CSV and TXT files.
- Flask web application development.
- HTML and CSS integration.
- Form handling and input validation.
- Basic financial calculations.

## ⚠️ Disclaimer
This project uses predefined sample stock prices stored in a Python dictionary. It does not fetch live stock-market prices and is developed for educational purposes only. It is not intended for actual investment decisions.

## 🎓 Internship Project
**Internship Organization:** CodeAlpha
**Domain:** Python Programming
**Project:** Stock Portfolio Tracker

## 👨‍💻 Author
**Sudarshan Kalashetty**
Computer Science and Design Student
---

⭐ If you find this project useful, feel free to explore the repository and share your feedback!

#Python #Flask #StockPortfolioTracker #CodeAlpha #PythonInternship #WebDevelopment
