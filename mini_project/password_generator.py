import string
import random

all_letters_list = list(string.ascii_letters)
symbols_list = list(string.punctuation)
combined = all_letters_list + symbols_list



num = int(input("How much characters do you want to pick for your password: "))
generate = random.choices(combined,k=num)
word = ''.join(generate)
print(word)


