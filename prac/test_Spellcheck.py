import pytest
from spellcheck import word_count, char_count, first_char, last_char

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string has fewer than 10 words
        2. Use an assert statement to check the given string has fewer than 50 chars

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    # Check the number of words in the string
    word_count_result = word_count(input_value)
    assert word_count_result < 10, "The string should have fewer than 10 words."

    # Check the number of characters in the string
    char_count_result = char_count(input_value)
    assert char_count_result < 50, "The string should have fewer than 50 characters."

# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string begins with a capital letter
        2. Use an assert statement to check the given string ends with a period ('.')

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    # Check the first character of the string
    first_char_result = first_char(input_value)
    assert first_char_result.isupper(), "The string should start with a capital letter."

    # Check the last character of the string
    last_char_result = last_char(input_value)
    assert last_char_result == '.', "The string should end with a period."

# Run these tests with `python3 -m pytest test_spellcheck.py`
