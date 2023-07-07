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
import json

import requests

RACECAR = "racecar"


def test_correctly_identifies_a_palindrome():
    """Validate palindrome endpoint correctly identifies a palindrome"""

    # Fill in code to fetch the actual is_palindrome value from application
    response = requests.post("http://localhost:8080/palindrome", json={"word": RACECAR})
    assert response, "No response"
    assert response.text, "Text is where the response is stored. It's not there!"
    response = json.loads(response.text)
    assert response["is_palindrome"], f"{RACECAR} is a palindrome! What gives!"
