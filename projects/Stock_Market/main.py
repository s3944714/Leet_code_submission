# ============================================================
# STOCK MARKET SIMULATOR - PROJECT SPEC
# Turn-based (day-by-day) trading game vs. market dynamics,
# with difficulty levels, data science elements, and algorithms
# ============================================================
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
# - Basic statistics (moving averages, volatility, % change)
# - Algorithms (trend detection, momentum calculation, sorting)
# - matplotlib (charting price history - added later, Phase 6)
#
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
print("-----Welcome to the stock market-----")
print(f"You begin the game with ${portfolio['CASH']} Dollars")
print(f"The game runs on: {total_days} days")
print("The Price moves each day based on the market simulation")
print(f"Your goal: maximize your net worth by the end of the {total_days} days")



# 1. Create a starting cash balance (e.g. 10,000) stored in a
#    variable or a portfolio dictionary.
# 2. Create a dictionary of stocks, each with a starting price
#    and a "trend bias" that will influence how its price moves.
#    e.g. {"TECH": {"price": 150.00, "volatility": 0.03, "trend": 0.001}, ...}
#    Use at least 4-5 fictional tickers with different starting
#    prices, volatility, and trend characteristics (one stable,
#    one volatile, one trending up, one trending down).
# 3. Create a portfolio dictionary tracking shares owned per stock:
#    {"TECH": 0, "FOOD": 0, "ENRG": 0, ...}
# 4. Create a price_history dictionary that will store each day's
#    closing price per stock, e.g. {"TECH": [150.00], "FOOD": [...], ...}
#    - seed each list with the starting price from step 2.
# 5. Print a welcome message explaining the rules: starting cash,
#    how many trading days the game will run, that prices move
#    each day based on market simulation, and the goal (maximize
#    net worth by game end).
#
# ------------------------------------------------------------
# PHASE 2 - Difficulty levels
# ------------------------------------------------------------
# 1. Ask the player to choose a difficulty at the start of the
#    game (e.g. "easy", "normal", "hard").
# 2. Difficulty should affect how unpredictable the market is:
#    - Easy: lower volatility, price trends are more consistent
#      and easier to read day-to-day.
#    - Normal: moderate volatility, occasional sharp moves.
#    - Hard: high volatility, frequent random shocks/news events
#      (see Phase 4) that can swing prices sharply either way.
# 3. Store the chosen difficulty and use it as a multiplier or
#    parameter inside your price-update function (Phase 3) - e.g.
#    scale each stock's "volatility" value up or down depending
#    on difficulty before calculating the day's price change.
#
# ------------------------------------------------------------
# PHASE 3 - Daily price simulation (one "day" = one loop iteration)
# ------------------------------------------------------------
# 1. Write a function update_price(stock_data, difficulty) that:
#    - Takes one stock's info dictionary (price, volatility, trend)
#      and the difficulty setting
#    - Calculates a random daily % change using the stock's
#      volatility (scaled by difficulty) and trend bias
#    - Applies that % change to the current price
#    - Returns the new price
# 2. Write a function simulate_day(stocks, price_history, difficulty)
#    that:
#    - Loops through every stock in the stocks dictionary
#    - Calls update_price() for each one
#    - Updates that stock's current price
#    - Appends the new price onto price_history for that stock
# 3. Print a simple day summary after each simulated day: each
#    stock's ticker, new price, and % change from the previous day.
#
# ------------------------------------------------------------
# PHASE 4 - Player actions each day
# ------------------------------------------------------------
# 1. Each day, before (or after) prices update, show the player:
#    - Current cash balance
#    - Current holdings (shares per stock) and their current value
#    - Current prices for all stocks
# 2. Present a menu of actions:
#    - Buy shares of a stock
#    - Sell shares of a stock
#    - View price history / stats for a stock (Phase 5)
#    - Do nothing / advance to next day
# 3. Buy logic: ask which stock and how many shares; validate
#    they have enough cash (shares * current_price <= cash);
#    deduct cash, add shares to portfolio.
# 4. Sell logic: ask which stock and how many shares; validate
#    they actually own at least that many shares; add cash,
#    subtract shares from portfolio.
# 5. Random news events (optional but recommended, ties into
#    difficulty): occasionally (more often on "hard") trigger a
#    random event affecting one stock significantly for that day
#    (e.g. "TECH just released a breakthrough product! +15%" or
#    "FOOD recalled products - -10%"), applied as an extra
#    multiplier on top of the normal daily price update.
#
# ------------------------------------------------------------
# PHASE 5 - Data science elements
# ------------------------------------------------------------
# 1. Write a function moving_average(price_list, window) that:
#    - Takes a stock's price history list and a window size (e.g. 5)
#    - Returns the average of the last `window` prices
#    - Used to smooth out noise and show the player a trend line
# 2. Write a function percent_change(price_list) that returns the
#    % change from the first recorded price to the most recent one
#    (overall performance of a stock across the whole game so far).
# 3. Write a function volatility_score(price_list) that calculates
#    how much a stock's price has fluctuated (e.g. standard
#    deviation of daily % changes, or simpler: average absolute
#    day-to-day % change) - gives the player a "riskiness" rating.
# 4. Add a "View stats" menu option (from Phase 4) that, for a
#    chosen stock, prints: current price, moving average, overall
#    % change since day 1, and volatility score.
#
# ------------------------------------------------------------
# PHASE 6 - Visualization (matplotlib, added later)
# ------------------------------------------------------------
# 1. Import matplotlib.pyplot.
# 2. Write a function plot_stock(ticker, price_history) that plots
#    one stock's full price history as a line chart, with day
#    number on the x-axis and price on the y-axis.
# 3. Write a function plot_all_stocks(price_history) that plots
#    every stock's price history on the same chart for comparison
#    (multiple lines, one per ticker, with a legend).
# 4. Add a "chart" option to the Phase 4 menu that lets the player
#    pull up a chart for a specific stock, or all stocks, at any
#    point during the game.
# 5. At game end, automatically display a final chart summarizing
#    all stocks' full price movement across the game.
#
# ------------------------------------------------------------
# PHASE 7 - Turn loop and end-game
# ------------------------------------------------------------
# 1. Decide a total number of trading days (e.g. 30 or 60) -
#    could be difficulty-dependent (fewer days = easy, more days
#    = hard, or vice versa depending on how you want difficulty
#    to feel).
# 2. Wrap Phases 3 and 4 in a loop that runs once per day: show
#    state -> player takes action(s) -> simulate_day() updates
#    prices -> repeat until day count is reached.
# 3. At game end, compute final net worth = cash + (shares owned
#    x current price, summed across all stocks).
# 4. Print an end-game summary: final net worth, total return
#    (% change from starting cash), best-performing stock in the
#    player's portfolio, worst-performing stock.
# 5. Trigger the Phase 6 final chart display.
#
# ------------------------------------------------------------
# PHASE 8 - Hourly trading week (advanced turn structure)
# ------------------------------------------------------------
# Only tackle this after Phases 1-4 (daily-turn MVP) and the
# AI bot trader phase are fully working and tested.
#
# 1. Redefine one "turn" as one hour instead of one day. Define
#    a trading window per day (e.g. 7 trading hours), across a
#    5-day trading week - so a week = 5 x 7 = 35 turns instead
#    of 5.
# 2. Restructure price_history to store one price per hour, not
#    per day - e.g. price_history["STBL"] grows by one entry
#    every turn instead of once per day. Consider nesting by day
#    if you want to keep day-level structure visible (e.g. a
#    list of lists, one sub-list per day), or keep it as one
#    flat list and track day boundaries separately.
# 3. Scale volatility down per-hour so a full day's worth of
#    hourly moves doesn't wildly exceed your original daily
#    volatility - e.g. divide each stock's daily volatility by
#    the number of trading hours per day, or by the square root
#    of that number (statistically closer to how real volatility
#    scaling works), and use that scaled-down value inside
#    update_price() instead of the daily one.
# 4. Decide and implement what "unlimited actions" means for a
#    single hour - e.g. multiple buy/sell actions allowed before
#    the hour's price updates, or a fixed single decision point
#    per hour with the option to act every turn instead of once
#    per day.
# 5. Update the Phase 7 game loop: outer loop over trading days,
#    inner loop over trading hours within each day, calling
#    update_price() and the player-action menu once per hour
#    instead of once per day.
# 6. Update end-game summary and charts (Phase 6) to reflect the
#    much larger number of data points - may want an option to
#    view a daily "close" chart (one point per day, using the
#    last hourly price of each day) alongside the full hourly
#    detail chart.
#
# ------------------------------------------------------------
# STRETCH GOALS
# ------------------------------------------------------------
# - Add a simple "market index" (average of all stock prices)
#   that the player's performance gets benchmarked against -
#   "you beat/underperformed the market by X%."
# - Add dividends: some stocks randomly pay out a small % of
#   share value as bonus cash on certain days.
# - Add short-selling as an advanced action (bet on a price drop).
# - Add a basic "algorithm" mode: an optional auto-trader using a
#   simple rule (e.g. moving-average crossover: buy when short-term
#   average crosses above long-term average, sell when it crosses
#   below) that the player can toggle on to see how it performs
#   compared to their own manual trading.
# - Save game history (all days' prices + trades) to a CSV file
#   using Python's built-in csv module for later analysis.
#
# ============================================================