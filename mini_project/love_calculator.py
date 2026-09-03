"""
Love Calculator
===============
Write a function called calculate_love_score() that tests the
compatibility between two names.

To work out the love score between two people:
1. Take both people's names combined and count how many times the
   letters T, R, U, E occur (in total, across both names).
2. Then count how many times the letters L, O, V, E occur (in total,
   across both names).
3. Combine these two counts to make a 2 digit number and print it out.

e.g.
    name1 = "Angela Yu"
    name2 = "Jack Bauer"

    T occurs 0 times
    R occurs 1 time
    U occurs 2 times
    E occurs 2 times
    Total = 5

    L occurs 1 time
    O occurs 0 times
    V occurs 0 times
    E occurs 2 times
    Total = 3

    Love Score = 53

Example:
    Input:  calculate_love_score("Kanye West", "Kim Kardashian")
    Output: 42

Since Udemy's exercise environment has no console, input() can't be used.
Test by calling the function with hard-coded values, e.g.
calculate_love_score("Kanye West", "Kim Kardashian")
"""

def calculate_love_score(name1: str, name2: str) -> str:
    cname = "".join([name1, name2]).replace(" ", "").lower()
    target_letters_true = {"t","r","u","e"}
    target_letters_love = {"l","o","v","e"}
    true_total_count = sum(char in target_letters_true for char in cname)
    love_total_count = sum(char in target_letters_love for char in cname)
    love_score = str(true_total_count) + str(love_total_count)
    return (f"The love score should be {love_score}")

print(calculate_love_score("Kanye West", "Kim Kardashian"))
