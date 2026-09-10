# ============================================================
# AI AUCTION SYSTEM CLI - PROJECT SPEC
# You vs. a Python "AI" bot, bidding on items with starting balances
# ============================================================

import random

# ------------------------------------------------------------
# PHASE 1 - Setup
# ------------------------------------------------------------
balances = {
    "user": 1000,
    "bot": 1000
}

# Ownership tracking - each player's list of won items
ownership = {
    "user": [],
    "bot": []
}

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

print("-----------Auction System------------------")
print("Welcome to the Auction House")
print("--------------Rules------------------")
print("One item will be bidded at a time, and the highest bid will win.")


# ------------------------------------------------------------
# PHASE 2 - Single-item round
# ------------------------------------------------------------
def single_item(item):
    for key, value in item.items():
        print(f"{key}: {value}")
    print("_" * 20)
    return item


def user_bid(current_balance):
    while True:
        try:
            bidding = int(input("Enter your bid: "))
            if bidding > current_balance:
                print(f"The bid is too high, your current balance is :{current_balance}")
            else:
                print("Valid Bid")
                return bidding
        except ValueError:
            print("This is not a valid number")


def bot_decide_bid(item, bot_balance):
    bot_bid = random.randint(0, bot_balance)
    return bot_bid


# ------------------------------------------------------------
# PHASE 3 - Multi-item loop
# ------------------------------------------------------------
def run_round(item, balances, ownership):
    single_item(item)

    if balances["user"] <= 0:
        user_amount = 0
    else:
        user_amount = user_bid(balances["user"])

    if balances["bot"] <= 0:
        bot_amount = 0
    else:
        bot_amount = bot_decide_bid(item, balances["bot"])

    if user_amount < bot_amount:
        print(f"Computer has won with a bid of {bot_amount}")
        balances["bot"] -= bot_amount
        print(f"Bot Balance is {balances['bot']}")
        ownership["bot"].append(item["name"])
    elif user_amount > bot_amount:
        print(f"you have won with a bid of {user_amount}")
        balances["user"] -= user_amount
        print(f"user Balance is {balances['user']}")
        ownership["user"].append(item["name"])
        
    else:
        print("No one wins")

    return


for item in auction_storage:
    run_round(item, balances, ownership)
print(f"The user has won {ownership['user']} and his current balance is : {balances['user']}")
print(f"The bot has won {ownership['bot']} and his current balance is : {balances['bot']}")
    

# TODO Phase 3, Step 4: after the loop finishes, print a summary
# of what each player won (from `ownership`) and their final
# balances (from `balances`)


# ------------------------------------------------------------
# PHASE 4 - Bot logic (pick a level)
# ------------------------------------------------------------
# - Simple: bot bids a random amount between 0 and its remaining
#   balance (random.uniform).
# - Medium: bot bids a percentage of the item's true_value
#   (e.g. up to 90%), capped by its remaining balance.
# - Smart (stretch): bot factors in items remaining and budget
#   left, so it doesn't blow its whole balance on the first item.
def bot_level(bot_balance):
    simple_bot = random.randint(0, bot_balance)
    percentage = 90
    medium_bot = bot_balance * (percentage / 100)

# ------------------------------------------------------------
# PHASE 5 - Scoring / end-game
# ------------------------------------------------------------
# 1. Compute each player's net worth = remaining cash + sum of
#    true_value of items they won.
# 2. Declare a winner based on net worth.
# 3. Optional: print a table showing item-by-item who bid what.

# ------------------------------------------------------------
# STRETCH GOALS
# ------------------------------------------------------------
# - Multiple bots with different personalities.
# - Bot "learns" your average bid-to-value ratio and adapts.
# - Add a difficulty setting.