# ============================================================
# STOCK MARKET SIMULATOR - PROJECT SPEC
# Turn-based (day-by-day) trading game vs. market dynamics,
# with difficulty levels, data science elements, and algorithms
# ============================================================
#
# PROGRESS
# [x] Phase 1 - Setup
# [x] Phase 2 - Difficulty levels
# [x] Phase 3 - Daily price simulation
# [x] Phase 4 - Player actions (status, menu, buy, sell, news events)
# [x] Phase 5 - Data science (moving average, % change, volatility, stats menu)
# [ ] Phase 6 - matplotlib charts
# [ ] Phase 7 steps 3-5 - end-game summary (net worth, return, best/worst)
# [ ] Phase 8 - hourly trading week
# [ ] Stretch goals / AI bot trader
#
# CONCEPTS USED:
# - Variables & data types (float for prices/cash, int for shares/days)
# - Control flow (if/elif/else)
# - Lists (price history, day-by-day records)
# - Loops (while/for loops - one iteration per trading day)
# - Functions (breaking program into reusable pieces)
# - Dictionaries & nested dictionaries (portfolio, stock data)
# - Function parameters & return values
# - random module (price movement simulation)
# - numpy (mean, diff, std for the stats functions)
# - matplotlib (charting price history - added later, Phase 6)
#
import random
import numpy as np

# ------------------------------------------------------------
# PHASE 1 - Setup
# ------------------------------------------------------------
total_days = 30
stocks = {
    # Blue-chip style: High starting price, low volatility, flat trend
    "STBL": {
        "price": 250.00,
        "volatility": 0.005,
        "trend": 0.000
    },

    # Growth/Tech style: Moderate price, moderate volatility, strong upward bias
    "MOON": {
        "price": 85.50,
        "volatility": 0.020,
        "trend": 0.004
    },

    # Distressed/Short target: Lower price, high volatility, downward bias
    "SINK": {
        "price": 42.10,
        "volatility": 0.035,
        "trend": -0.003
    },

    # Crypto/Meme style: Low starting price, extreme volatility, chaotic but slightly upward
    "RSTR": {
        "price": 12.75,
        "volatility": 0.080,
        "trend": 0.001
    },

    # Defensive/Income style: Steady price, very low volatility, slight upward drift (inflation-paced)
    "SAFE": {
        "price": 110.20,
        "volatility": 0.008,
        "trend": 0.0005
    }
}

portfolio = {
    "CASH": 10000.00,
    "STBL": 0,
    "MOON": 0,
    "SINK": 0,
    "RSTR": 0,
    "SAFE": 0,
}

price_history = {
    "STBL": [stocks["STBL"]["price"]],
    "MOON": [stocks["MOON"]["price"]],
    "SINK": [stocks["SINK"]["price"]],
    "RSTR": [stocks["RSTR"]["price"]],
    "SAFE": [stocks["SAFE"]["price"]],
}

news_events = [
    {"headline": "{ticker} announces breakthrough product launch next week!", "impact": 0.18},
    {"headline": "{ticker} facing a regulatory investigation.", "impact": -0.15},
    {"headline": "{ticker} reports earnings far above expectations.", "impact": 0.12},
    {"headline": "{ticker} issues a profit warning to investors.", "impact": -0.14},
    {"headline": "{ticker} secures a major new partnership deal.", "impact": 0.10},
    {"headline": "{ticker} recalls a defective product line.", "impact": -0.20},
    {"headline": "{ticker} announces an unexpected executive resignation.", "impact": -0.08},
    {"headline": "{ticker} wins a significant industry award.", "impact": 0.07},
    {"headline": "{ticker} is rumored to be an acquisition target.", "impact": 0.22},
    {"headline": "{ticker} suffers a major data breach.", "impact": -0.18},
]
pending_events = []

print("-----Welcome to the stock market-----")
print(f"You begin the game with ${portfolio['CASH']:.2f}")
print(f"The game runs on: {total_days} days")
print("The Price moves each day based on the market simulation")
print(f"Your goal: maximize your net worth by the end of the {total_days} days")


# ------------------------------------------------------------
# PHASE 2 - Difficulty levels
# ------------------------------------------------------------
while True:
    choice = input("Enter the difficulty level (Easy, Medium, Hard): ").strip().lower()
    if choice == "easy":
        difficulty_multiplier = 0.5
        break
    elif choice == "medium":
        difficulty_multiplier = 1.5
        break
    elif choice == "hard":
        difficulty_multiplier = 3.0
        break
    else:
        print("Invalid word, try again")


# ------------------------------------------------------------
# PHASE 3 - Daily price simulation
# ------------------------------------------------------------
def update_price(stock_data, difficulty):
    scaled_volatility = stock_data["volatility"] * difficulty
    daily_pct_change = stock_data["trend"] + random.gauss(0, scaled_volatility)
    stock_data["price"] = stock_data["price"] * (1 + daily_pct_change)
    return daily_pct_change, stock_data["price"]


def simulate_day(stocks, price_history, difficulty):
    print("\nSummary of the Day")
    for ticker, data in stocks.items():
        pct_change, new_price = update_price(data, difficulty)
        price_history[ticker].append(new_price)
        print(f"{ticker}: ${new_price:.2f} ({pct_change * 100:.2f}% change)")
    return


# ------------------------------------------------------------
# PHASE 4 - Player actions each day
# ------------------------------------------------------------
def show_daily_status(day, portfolio, stocks):
    print(f"\n----- Day {day} -----")
    print(f"Cash: ${portfolio['CASH']:.2f}")
    print("-" * 40)
    for ticker, data in stocks.items():
        shares = portfolio[ticker]
        value = shares * data["price"]
        print(f"{ticker}: ${data['price']:.2f} | {shares} shares, worth ${value:.2f}")
    print("-" * 40)
    return


def player_menu():
    print("What would you like to do?")
    print("1. Buy shares")
    print("2. Sell shares")
    print("3. View price history / stats for a stock")
    print("4. Do nothing / advance to next day")
    choice = input("Enter your choice (1-4): ").strip()
    return choice


def buy_stock(portfolio, stocks):
    ticker = input("Which stock do you want to buy? ").strip().upper()
    if ticker not in stocks:
        print("Not a valid Stock")
        return
    try:
        shares = int(input("How many shares do you want to buy? "))
        if shares <= 0:
            print("You must buy at least 1 share")
            return
    except ValueError:
        print("Enter a valid whole number")
        return
    cost = shares * stocks[ticker]["price"]
    if cost > portfolio["CASH"]:
        print(f"Try again, you do not have enough cash, it would cost ${cost:.2f}, you have ${portfolio['CASH']:.2f}")
        return
    portfolio["CASH"] -= cost
    portfolio[ticker] += shares
    print(f"Bought {shares} shares of {ticker} for ${cost:.2f}.")
    return


def sell_stock(portfolio, stocks):
    ticker = input("Which stock do you want to sell? ").strip().upper()
    if ticker not in stocks:
        print("Not a valid Stock")
        return
    if ticker not in portfolio or portfolio[ticker] <= 0:
        print(f"You do not own any shares of {ticker}.")
        return

    try:
        shares = int(input("How many shares do you want to sell? "))
        if shares <= 0:
            print("You must sell at least 1 share")
            return
    except ValueError:
        print("Enter a proper value")
        return

    if shares > portfolio[ticker]:
        print(f"You cannot sell {shares} shares. You only own {portfolio[ticker]} shares of {ticker}.")
        return

    proceeds = shares * stocks[ticker]["price"]
    portfolio[ticker] -= shares
    portfolio["CASH"] += proceeds
    print(f"Sold {shares} shares of {ticker} for ${proceeds:.2f}.")
    return


def announce_news(stocks, news_events, pending_events, day, difficulty):
    base_chance = 0.05
    chance = base_chance * difficulty

    if random.random() < chance:
        ticker = random.choice(list(stocks.keys()))
        event = random.choice(news_events)
        headline = event["headline"].format(ticker=ticker)
        print(f"NEWS: {headline}")

        pending_events.append({
            "ticker": ticker,
            "impact": event["impact"],
            "trigger_day": day + 1
        })
    return


def trigger_news(stocks, pending_events, day):
    still_pending = []
    for event in pending_events:
        if event["trigger_day"] == day:
            ticker = event["ticker"]
            impact = event["impact"]
            stocks[ticker]["price"] = stocks[ticker]["price"] * (1 + impact)
            print(f"The rumored news about {ticker} has come true! Price moved {impact * 100:.1f}%")
        else:
            still_pending.append(event)
    return still_pending


# ------------------------------------------------------------
# PHASE 5 - Data science elements (numpy)
# ------------------------------------------------------------
def moving_average(price_list, window):
    # Slice the last `window` prices, then average them
    recent_prices = price_list[-window:]
    return np.mean(recent_prices)


def percent_change(price_list):
    # Overall % change from the first recorded price to the latest
    first_price = price_list[0]
    latest_price = price_list[-1]
    change = (latest_price - first_price) / first_price
    return change * 100


def volatility_score(price_list):
    # Need at least 2 prices to have one day-to-day change
    if len(price_list) < 2:
        return 0.0
    prices = np.array(price_list)
    daily_changes = np.diff(prices)            # differences between consecutive days
    pct_changes = daily_changes / prices[:-1]  # convert to % change vs the "before" price
    return np.std(pct_changes) * 100


def view_stats(stocks, price_history):
    ticker = input("Which stock do you want stats for? ").strip().upper()
    if ticker not in stocks:
        print("Not a valid Stock")
        return
    prices = price_history[ticker]
    print(f"\n----- {ticker} Stats -----")
    print(f"Current price:      ${stocks[ticker]['price']:.2f}")
    print(f"5-day moving avg:   ${moving_average(prices, 5):.2f}")
    print(f"Change since day 1: {percent_change(prices):.2f}%")
    print(f"Volatility score:   {volatility_score(prices):.2f}")
    print("-" * 40)
    return


def run_day(day, portfolio, stocks, price_history):
    show_daily_status(day, portfolio, stocks)
    while True:
        choice = player_menu()
        if choice == "1":
            buy_stock(portfolio, stocks)
        elif choice == "2":
            sell_stock(portfolio, stocks)
        elif choice == "3":
            view_stats(stocks, price_history)
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again")
    return


# ------------------------------------------------------------
# PHASE 6 - Visualization (matplotlib, added later)
# ------------------------------------------------------------
# 1. Import matplotlib.pyplot.
# 2. plot_stock(ticker, price_history): one stock's line chart.
# 3. plot_all_stocks(price_history): every stock on one chart with a legend.
# 4. Add a "chart" option to the player menu.
# 5. At game end, display a final chart of all stocks.
#
# ------------------------------------------------------------
# PHASE 7 (steps 3-5) - End-game summary
# ------------------------------------------------------------
# TODO: after the loop below finishes, compute and print:
# - final net worth = cash + sum(shares x current price)
# - total return % vs starting cash
# - best and worst performing stock in the player's portfolio
# - trigger the Phase 6 final chart
#
# ------------------------------------------------------------
# PHASE 8 - Hourly trading week (advanced turn structure)
# ------------------------------------------------------------
# Only after the daily-turn game and the AI bot trader are working.
# - One turn = one hour, 7 trading hours x 5 days = 35 turns
# - Scale volatility per hour (divide by sqrt of hours per day)
# - Nested loop: days -> hours; update price_history hourly
#
# ------------------------------------------------------------
# STRETCH GOALS
# ------------------------------------------------------------
# - AI bot trader alongside the player (optional trade-impact on prices)
# - Market index benchmark
# - Dividends
# - Short-selling
# - Moving-average crossover auto-trader
# - Save game history to CSV
#
# ============================================================


# ------------------------------------------------------------
# MAIN GAME LOOP (Phase 7, steps 1-2)
# ------------------------------------------------------------
for day in range(1, total_days + 1):
    run_day(day, portfolio, stocks, price_history)
    announce_news(stocks, news_events, pending_events, day, difficulty_multiplier)
    pending_events = trigger_news(stocks, pending_events, day)
    simulate_day(stocks, price_history, difficulty_multiplier)