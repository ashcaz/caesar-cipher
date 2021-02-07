import nltk
from string import ascii_lowercase, ascii_uppercase

alphabet_lower = dict(zip(ascii_lowercase, range(1, 27)))  # found this on stackoverflow
print(alphabet_lower)

alphabet_upper = dict(zip(ascii_uppercase, range(1, 27)))


def encrypt(text_phrase: str, key: int) -> str:

    if type(text_phrase) != str or type(key) != int:
        raise TypeError(
            "Please enter a valid string and a valid integer for this method"
        )

    encrypted_text = ""

    for char in text_phrase:
        if char == " ":
            encrypted_text += char
        elif char.islower():
            new_value = alphabet_lower[char] + key
            if new_value > 26:
                new_value = new_value % 26

            for k in alphabet_lower.keys():
                if new_value == alphabet_lower[k]:
                    encrypted_text += k
        elif char.isupper():
            new_value = alphabet_upper[char] + key

            for k in alphabet_upper.keys():
                if new_value == alphabet_upper[k]:
                    encrypted_text += k
        else:
            raise Exception(
                "The text phrase inclues unknown characters. Phrases must be all letters."
            )

    return encrypted_text


def decrypt(text_phrase: str, key: int) -> str:
    # use encypt with -key
    pass


def crack(text_phrase: str, key: int) -> str:
    pass
