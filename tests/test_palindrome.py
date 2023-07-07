"""
Write tests for application endpoint palindrome
A palindrome is a word, phrase, or sequence that reads the same backward as forward

Request Info:

POST to http://localhost:8080/palindrome
header: Content-Type application/json
Request body: { "word": "racecar" }

Sample Response:
{
    "is_palindrome": false,
    "word": "23444"
}
"""


def test_correctly_identifies_a_palindrome():
    """Validate palindrome endpoint correctly identifies a palindrome"""
    actual_value = None

    # Fill in code to fetch the actual is_palindrome value from application

    assert actual_value
