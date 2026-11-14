# Equity — Stock Portfolio Tracker

A simple stock portfolio tracker website built with Python and Flask for the assignment.

## Features
- User enters share quantities for manually selected stock symbols.
- Uses a hardcoded Python dictionary for sample prices.
- Calculates each holding: `quantity × price`.
- Calculates the total investment value.
- Saves the result automatically to CSV and TXT files.
- Allows the user to download either report.

## Technologies / concepts
- Python dictionary (`STOCK_PRICES`)
- Input and output
- Basic arithmetic
- File handling (`open`, CSV writer)
- Flask, HTML and CSS for the website

## Run on Windows
1. Extract the ZIP.
2. Open the folder in VS Code or Command Prompt.
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   py -m venv venv
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the website:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

## Run on macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Then open `http://127.0.0.1:5000`.

## Sample prices
AAPL $180, TSLA $250, GOOGL $140, MSFT $420, AMZN $185, NVDA $120,
META $500, NFLX $610, RELIANCE ₹2950 (stored as numeric sample value),
TCS ₹3900, INFY ₹1450, HDFCBANK ₹1650.

For simplicity, this demo displays a `$` symbol for all sample prices.
These values are hardcoded examples, not live market prices or investment advice.

## Generated output
- `data/portfolio.csv`
- `data/portfolio_summary.txt`

The latest calculation overwrites the previous report.
