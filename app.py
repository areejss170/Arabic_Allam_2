from flask import Flask, request, jsonify , render_template
from flask_cors import CORS
from Test2 import generate_answer # Replace with your grammar model implementation

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/check_grammar', methods=['POST'])
def check_grammar():
    data = request.json
    input_text = data.get('text', '')

    # Use your grammar-checking model here
    corrected_text = generate_answer(input_text)  # Assuming your model has a function to correct grammar

    return jsonify({"corrected_text": corrected_text})

if __name__ == "__main__":
    app.run()
