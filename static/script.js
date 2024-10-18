async function checkGrammar() {
    const text = document.getElementById('text-input').value;  // Get user input

    // Send a POST request to the Flask API
    const response = await fetch('http://127.0.0.1:5000/check_grammar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })  // Send the text as JSON
    });

    const result = await response.json();  // Get the response (corrected text)
    
    // Display the corrected text in the HTML
    document.getElementById('result').textContent = result.corrected_text;
}
