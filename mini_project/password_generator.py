import string
import random

easy_chars = list(string.ascii_lowercase + string.digits)
hard_chars = list(string.ascii_letters + string.punctuation) 



num = int(input("How much characters do you want to pick for your password: "))
user_level= input("Enter User level: ").lower()


def generate_password(length: int, level: str) -> str:
    if length <= 0:
        return "invalid length"

    if level == "easy":
        generate = random.choices(easy_chars,k=num)
        word = ''.join(generate)
        return word
    if level == "hard":
        generate = random.choices(hard_chars,k=num)
        word = ''.join(generate)
        return word

password = generate_password(num, user_level)
print(password)