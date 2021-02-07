import nltk
from string import ascii_lowercase, ascii_uppercase

alphabet_lower = ascii_lowercase

alphabet_upper = ascii_uppercase


def encrypt(text_phrase: str, key: int) -> str:

    if type(text_phrase) != str or type(key) != int:
        raise TypeError(
            "Please enter a valid string and a valid integer for this method"
        )

    encrypted_text = ""

    for char in text_phrase:
        if char == " ":
            encrypted_text += char
        else:
            if char.islower():
                alphabet = alphabet_lower
            elif char.isupper():
                alphabet = alphabet_upper
            else:
                raise Exception(
                    "The text phrase inclues unknown characters. Phrases must be all letters."
                )

            new_value = alphabet.index(char) + key

            if new_value > 25 or new_value < -25:
                new_value = new_value % 26

            if new_value < 0:
                new_value = new_value + 26

            encrypted_text += alphabet[new_value]

    return encrypted_text


def decrypt(text_phrase: str, key: int) -> str:

    decyrpted_message = encrypt(text_phrase, -key)
    return decyrpted_message


def crack(text_phrase: str, key: int) -> str:
    pass
