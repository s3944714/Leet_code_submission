"""
Life in Weeks
=============
Based on the article by Tim Urban - Your Life in Weeks:
https://waitbutwhy.com/2014/05/life-weeks.html

It's a reminder of just how little time we actually have.

This exercise:
Create a function called life_in_weeks() that uses maths and f-strings
to tell us how many weeks we have left, assuming we live until age 90.

The function takes your current age as input and outputs a message in
this exact format:

    You have x weeks left.

Where x is the calculated number of weeks remaining until age 90.

Note: the function must be named exactly `life_in_weeks`, and the output
punctuation/spelling must match the example exactly (including the full stop).

Example:
    Input:  56
    Output: You have 1768 weeks left.

Since Udemy's exercise environment has no console, input() can't be used.
Test by calling the function with hard-coded values, e.g. life_in_weeks(12)
"""

def life_in_weeks(age):
    life = 90 - age
    calculate = life * 52
    print(f"You have {calculate} weeks left.")
    return calculate
life_in_weeks(20)
