import string
import random

def generate_password(query_password_length = 10) -> str:
    choices = string.ascii_letters + string.digits + r"""#$%&'()*+,-./:;=?@[\]^_`{|}~"""
    result = ""

    if not str(query_password_length).isdigit():
        raise TypeError("Invalid password length type...")

    query_password_length = int(query_password_length)

    for _ in range(query_password_length):
        result += random.choice(choices)
    return result 