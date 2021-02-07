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
def test_encrypt_num_in_phrase():
    with pytest.raises(Exception) as e:
        encrypt("str1ng", 5)
        print(str(e.value))
    assert (
        str(e.value)
        == "The text phrase inclues unknown characters. Phrases must be all letters."
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