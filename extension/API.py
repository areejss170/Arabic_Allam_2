from flask import Flask, request, jsonify
from Test2 import generate_answer
app = Flask(__name__)

# Import your grammar and rephrasing model here
# from your_model import grammar_checker, rephrasing_model

@app.route('/check', methods=['POST'])
def check_grammar_and_rephrase():
    data = request.json
    text = data.get('text')

    # Assuming your model functions are grammar_checker and rephrase
    # grammar_errors = grammar_checker(text)
    # rephrased_text = rephrase(text)

    # For now, just mock the results
    grammar_errors = {"errors": ["Example error 1", "Example error 2"]}
    rephrased_text = text[::-1]  # Just reverse the text for demo purposes

    response = {
        "grammar_errors": grammar_errors,
        "rephrased_text": rephrased_text
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
