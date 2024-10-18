function checkGrammarAndRephrase(text) {
    fetch('http://127.0.0.1:5000/check', {  // Use your deployed API URL
      method: 'POST',
      mode: 'no-cors', 
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
      console.log("Grammar Errors: ", data.grammar_errors);
      console.log("Rephrased Text: ", data.rephrased_text);
      
      // You can display the results in a popup or inline on the webpage
      showSuggestions(data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  
  function showSuggestions(data) {
    // Handle the display logic for grammar and rephrasing suggestions here
    // For example, you could create a popup window or highlight text on the page
  }
  document.addEventListener('mouseup', function() {
    let selectedText = window.getSelection().toString();
    if (selectedText) {
      checkGrammarAndRephrase(selectedText);
    }
  });
    