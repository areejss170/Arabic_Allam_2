document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.scripting.executeScript({
        target: {tabId: tabs[0].id},
        function: getSelectedText
      });
    });
  });
  
  function getSelectedText() {
    let selectedText = window.getSelection().toString();
    if (selectedText) {
      checkGrammarAndRephrase(selectedText);
    }
  }
  
  function checkGrammarAndRephrase(text) {
    fetch('http://your-api-domain.com/check', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('output').innerHTML = `
        <p>Grammar Errors: ${JSON.stringify(data.grammar_errors)}</p>
        <p>Rephrased Text: ${data.rephrased_text}</p>
      `;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  