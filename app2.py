from flask import Flask, request, jsonify
from grammerCheker import checker # Import your grammar checker model
from flask_cors import CORS
app = Flask(__name__) 
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS']='Content-Type'
@app.route('/check', methods=['POST','OPTIONS'])
def check_grammar():

     # Handle OPTIONS preflight request
    if request.method == 'OPTIONS':
        # Properly respond to the preflight request
        response = jsonify({'message': 'CORS preflight'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    if request.method == 'POST':
        data = request.json
        text = data.get('text', '')
        corrections = checker(text)  # Call your model to check grammar
        return jsonify(corrections)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Dummy function to simulate correction
# def correct_arabic_text(text):
#     corrected_text = text.replace("خطأ", "صحيح")  # Example correction
#     return corrected_text

# @app.route('/checker', methods=['POST'])
# def correct():
#     data = request.get_json()
#     text = data['text']
    
#     # Use your model to correct the text
#     corrected_text = correct_arabic_text(text)
    
#     # Return the corrected text as JSON
#     return jsonify({'correctedText': corrected_text})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
