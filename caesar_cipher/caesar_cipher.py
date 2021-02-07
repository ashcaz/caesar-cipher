from string import ascii_lowercase, ascii_uppercase
import nltk

nltk.download("words", quiet=True)
from nltk.corpus import words

alphabet_lower = ascii_lowercase
alphabet_upper = ascii_uppercase
word_list = words.words()


def encrypt(text_phrase: str, key: int) -> str:
    """[encrypts you phrase by shifting letters equal to the key]

    Args:
        text_phrase (str): [phrse you want to encrypt]
        key (int): [amount to shift]

    Raises:
        TypeError: [when phrase is not a str and when key is not an int]
        Exception: [When you use characters that are not a-z]

    Returns:
        str: [encypted phrase]
    """

    if type(text_phrase) != str or type(key) != int:
        raise TypeError(
            "Please enter a valid string and a valid integer for this method"
        )

    encrypted_text = ""

    for char in text_phrase:
        if not char.isalpha():
            encrypted_text += char
        else:
            if char.islower():
                alphabet = alphabet_lower
            elif char.isupper():
                alphabet = alphabet_upper

            new_value = alphabet.index(char) + key

            if new_value > 25 or new_value < -25:
                new_value = new_value % 26

            if new_value < 0:
                new_value = new_value + 26

            encrypted_text += alphabet[new_value]

    return encrypted_text


def decrypt(text_phrase: str, key: int) -> str:
    """[Will decrypt a phrase with the provided key]

    Args:
        text_phrase (str): [Phrase you want to decrypt]
        key (int): [amount to shift]

    Returns:
        str: [decrypted message]
    """

    decyrpted_message = encrypt(text_phrase, -key)
    return decyrpted_message


def crack(encrypted_phrase: str) -> str:

    for num in range(26):
        decrypted = decrypt(encrypted_phrase, num)
        decrypted_split = decrypted.split()
        return best_match
        # A little stuck on where to go from here
