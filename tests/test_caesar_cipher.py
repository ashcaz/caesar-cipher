import pytest
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack
from caesar_cipher import __version__


def test_version():
    assert __version__ == "0.1.0"


# @pytest.mark.skip("pending")
def test_encrypt_phrase_not_str():
    with pytest.raises(TypeError) as e:
        encrypt(5, 2)

    assert (
        str(e.value)
        == "Please enter a valid string and a valid integer for this method"
    )


# @pytest.mark.skip("pending")
def test_encrypt_key_not_int():
    with pytest.raises(TypeError) as e:
        encrypt("string", "5")

    assert (
        str(e.value)
        == "Please enter a valid string and a valid integer for this method"
    )


# @pytest.mark.skip("pending")
def test_encrypt_return_one(phrase_one):
    actual = encrypt(phrase_one, 1)
    expected = "bcd"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_encrypt_return_two(phrase_two):
    actual = encrypt(phrase_two, 1)
    expected = "yza"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_encrypt_return_three(phrase_three):
    actual = encrypt(phrase_three, 1)
    expected = "BtimfZ"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_encrypt_return_four(phrase_four):
    actual = encrypt(phrase_four, 1)
    expected = "J ibwf b Tfdsfu"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_decrypt_return_one(decode_phrase_1):
    actual = decrypt(decode_phrase_1, 1)
    expected = "abc"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_decrypt_return_two(decode_phrase_2):
    actual = decrypt(decode_phrase_2, 1)
    expected = "xyz"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_decrypt_return_three(decode_phrase_3):
    actual = decrypt(decode_phrase_3, 1)
    expected = "AshleY"
    assert actual == expected


def test_decrypt_return_four(decode_phrase_4):
    actual = decrypt(decode_phrase_4, 1)
    expected = "I have a Secret"
    assert actual == expected


def test_crack(quote):
    actual = crack(quote)
    expected = (
        "So, I love you because the entire universe conspired to help me find you."
    )
    assert actual == expected


#######################
# Fixtures
#######################


@pytest.fixture
def phrase_one():
    return "abc"


@pytest.fixture
def phrase_two():
    return "xyz"


@pytest.fixture
def phrase_three():
    return "AshleY"


@pytest.fixture
def phrase_four():
    return "I have a Secret"


@pytest.fixture
def decode_phrase_1():
    return "bcd"


@pytest.fixture
def decode_phrase_2():
    return "yza"


@pytest.fixture
def decode_phrase_3():
    return "BtimfZ"


@pytest.fixture
def decode_phrase_4():
    return "J ibwf b Tfdsfu"


@pytest.fixture
def quote():
    return "So, I love you because the entire universe conspired to help me find you."
