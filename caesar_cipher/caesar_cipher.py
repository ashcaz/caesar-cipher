import nltk
from string import ascii_lowercase, ascii_uppercase

alphabet_lower = dict(zip(ascii_lowercase, range(1, 27)))  # found this on stackoverflow
# print(alphabet_lower)

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
        else:
            if char.islower():
                dict_needed = alphabet_lower
            elif char.isupper():
                dict_needed = alphabet_upper
            else:
                raise Exception(
                    "The text phrase inclues unknown characters. Phrases must be all letters."
                )

            new_value = dict_needed[char] + key

            if new_value > 26 or new_value < -26:
                new_value = new_value % 26

            if new_value <= 0:
                new_value = new_value + 26

            for k in dict_needed.keys():
                if new_value == dict_needed[k]:
                    encrypted_text += k

    return encrypted_text


def decrypt(text_phrase: str, key: int) -> str:

    decyrpted_message = encrypt(text_phrase, -key)
    # print(-key)
    return decyrpted_message


def crack(text_phrase: str, key: int) -> str:
    pass


print(decrypt("BtimfZ", 1))
