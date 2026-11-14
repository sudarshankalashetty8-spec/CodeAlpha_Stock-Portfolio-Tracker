import csv
import os
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, send_file

app = Flask(__name__)
app.secret_key = "stock-tracker-demo-key"

# Hardcoded sample prices as requested in the assignment.
# These are demo prices, not live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 185.00,
    "NVDA": 120.00,
    "META": 500.00,
    "NFLX": 610.00,
    "RELIANCE": 2950.00,
    "TCS": 3900.00,
    "INFY": 1450.00,
    "HDFCBANK": 1650.00
}

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)
CSV_PATH = os.path.join(DATA_DIR, "portfolio.csv")
TXT_PATH = os.path.join(DATA_DIR, "portfolio_summary.txt")


def calculate_portfolio(form):
    holdings = []
    total_value = 0.0

    for symbol, price in STOCK_PRICES.items():
        raw_quantity = form.get(symbol, "").strip()
        if not raw_quantity:
            continue
        try:
            quantity = int(raw_quantity)
            if quantity < 0:
                raise ValueError
        except ValueError:
            raise ValueError(f"Enter a valid whole-number quantity for {symbol} (0 or more).")

        if quantity == 0:
            continue

        investment = quantity * price
        total_value += investment
        holdings.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

    return holdings, total_value


def save_portfolio(holdings, total_value):
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price per Share", "Investment Value"])
        for item in holdings:
            writer.writerow([
                item["symbol"],
                item["quantity"],
                f'{item["price"]:.2f}',
                f'{item["investment"]:.2f}'
            ])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", f"{total_value:.2f}"])

    with open(TXT_PATH, "w", encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write(f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        file.write("-" * 48 + "\n")
        for item in holdings:
            file.write(
                f'{item["symbol"]}: {item["quantity"]} shares x '
                f'${item["price"]:.2f} = ${item["investment"]:.2f}\n'
            )
        file.write("-" * 48 + "\n")
        file.write(f"TOTAL INVESTMENT: ${total_value:.2f}\n")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", stocks=STOCK_PRICES)


@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        holdings, total_value = calculate_portfolio(request.form)
    except ValueError as error:
        flash(str(error), "error")
        return redirect(url_for("index"))

    if not holdings:
        flash("Enter a quantity for at least one stock to calculate your portfolio.", "error")
        return redirect(url_for("index"))

    save_portfolio(holdings, total_value)
    return render_template(
        "result.html",
        holdings=holdings,
        total_value=total_value,
        stock_count=len(holdings),
        share_count=sum(item["quantity"] for item in holdings)
    )


@app.route("/download/<file_type>")
def download(file_type):
    if file_type == "csv":
        path = CSV_PATH
        filename = "portfolio.csv"
    elif file_type == "txt":
        path = TXT_PATH
        filename = "portfolio_summary.txt"
    else:
        flash("Unknown download format.", "error")
        return redirect(url_for("index"))

    if not os.path.exists(path):
        flash("Calculate a portfolio before downloading a report.", "error")
        return redirect(url_for("index"))
    return send_file(path, as_attachment=True, download_name=filename)


if __name__ == "__main__":
    app.run(debug=True)
