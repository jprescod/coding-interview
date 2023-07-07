from flask import Flask, request, jsonify

app = Flask(__name__)

def is_palindrome(word):
    """Checks if a word is a palindrome."""
    word = word.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return word == word[::-1]  # Compare the word with its reverse

@app.route('/', methods=['GET'])
def root():
    return "Hello World"


@app.route('/palindrome', methods=['POST'])
def check_palindrome():
    """Endpoint to check if a word is a palindrome."""
    data = request.get_json()
    word = data.get('word', '')

    if not word:
        return jsonify({'error': 'No word provided.'}), 400

    result = is_palindrome(word)

    return jsonify({'word': word, 'is_palindrome': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

