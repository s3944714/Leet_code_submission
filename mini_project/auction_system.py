# ============================================================
# AI AUCTION SYSTEM CLI - PROJECT SPEC
# You vs. a Python "AI" bot, bidding on items with starting balances
# ============================================================
#
# CONCEPTS USED:
# - Variables & data types (input casting to float/int)
# - Control flow (if/elif/else)
# - Lists (item order, ownership tracking)
# - Loops (while loops for repeated rounds)
# - Functions (breaking program into reusable pieces)
# - Dictionaries & nested dictionaries (core data structure)
# - Function parameters & return values
# - random module (for bot bidding logic)
#
# ------------------------------------------------------------
# PHASE 1 - Setup
# ------------------------------------------------------------
# 1. Create a balances dictionary: {"You": 1000, "Bot": 1000}
#    (or whatever starting number).
balances = {
    "user": 1000,
    "bot": 1000
}

# 2. Create a list/dict of auction items, each with a name and a
#    "true value" used only by the bot's logic, hidden from you.
#    e.g. {"name": "Painting", "true_value": 800}
auction_storage = [
    {"name": "Vintage 1968 Rolex Submariner", "true_value": 12500},
    {"name": "Signed Salvador Dalí Lithograph", "true_value": 3200},
    {"name": "1950s Fender Stratocaster Guitar", "true_value": 8500},
    {"name": "First Edition Harry Potter Book", "true_value": 45000},
    {"name": "Autographed Michael Jordan Jersey", "true_value": 6200},
    {"name": "Restored 1970s Pac-Man Arcade Cabinet", "true_value": 2500},
    {"name": "18K White Gold Diamond Necklace", "true_value": 5800},
    {"name": "Authentic 19th-Century Ship's Wheel", "true_value": 1200},
    {"name": "Tuscan Villa Week-Long Getaway", "true_value": 4000},
    {"name": "Life-Sized Replica Stormtrooper Armor", "true_value": 1800}
]

# 3. Print a welcome message explaining the rules (starting
#    balance, one item at a time, highest bid wins).
#

print("-----------Auction System------------------")
print("Welcome to the Auction House")
print("--------------Rules------------------")
print("One item will be bidded at a time, and the highest bid will win.")


# ------------------------------------------------------------
# PHASE 2 - Single-item round
# ------------------------------------------------------------
# 1. Show the item to both players.

def single_item(item):
    for key, value in item.items():
            print(f"{key}: {value}")
    print("_"*20)
    return item

# 2. Ask you for a bid (validate: must be a number, must not
#    exceed your current balance).
def bid(current_balance):
    while True:
        try:
            bidding = int(input("Enter your bid"))
            if bidding > current_balance:
                print(f"The bid is too high, your current balance is :{current_balance}")   
            else:
                print("Valid Bid")
                return bidding
        except ValueError:
            print("This is not a valid number")
    

    

# 3. Write bot_decide_bid(item, bot_balance) that:
#    - Takes item info and bot's remaining balance as parameters
#    - Returns a bid amount based on some logic (see Phase 4)
# 4. Compare your bid vs. the bot's bid.
# 5. Deduct the winning bid from the winner's balance in the
#    balances dict.
# 6. Print who won the item and for how much.
#
# ------------------------------------------------------------
# PHASE 3 - Multi-item loop
# ------------------------------------------------------------
# 1. Wrap Phase 2 in a while loop that runs once per item.
# 2. Before each round, check both balances - if a player can't
#    afford to bid, skip asking them or auto-set their bid to 0.
# 3. Track item ownership in a dictionary:
#    {"You": ["Painting"], "Bot": ["Vase"]}
# 4. After all items are gone, print a summary: what each player
#    won, and remaining balance.
#
# ------------------------------------------------------------
# PHASE 4 - Bot logic (pick a level)
# ------------------------------------------------------------
# - Simple: bot bids a random amount between 0 and its remaining
#   balance (random.uniform).
# - Medium: bot bids a percentage of the item's true_value
#   (e.g. up to 90%), capped by its remaining balance - won't
#   overpay for junk or underbid for something valuable.
# - Smart (stretch): bot factors in items remaining and budget
#   left, so it doesn't blow its whole balance on the first item.
#   e.g. max_bid = bot_balance / items_remaining * aggressiveness
#
# ------------------------------------------------------------
# PHASE 5 - Scoring / end-game
# ------------------------------------------------------------
# 1. Compute each player's net worth = remaining cash + sum of
#    true_value of items they won.
# 2. Declare a winner based on net worth (rewards smart bidding,
#    not just hoarding items).
# 3. Optional: print a table showing item-by-item who bid what.
#
# ------------------------------------------------------------
# STRETCH GOALS
# ------------------------------------------------------------
# - Multiple bots with different personalities (aggressive_bot,
#   cautious_bot) - practice writing similar functions with
#   different parameters.
# - Let the bot "learn" your average bid-to-value ratio over the
#   game and adjust its own bidding to counter you.
# - Add a difficulty setting that changes bot aggressiveness.
#
# ===========================================================


