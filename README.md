# Allam LLM Arabic Grammar Checker Chrome Extension
Overview
This Chrome extension uses Allam LLM, an advanced Arabic language model, to detect and correct grammar mistakes in Arabic text. The extension enhances Arabic writing by providing accurate grammar corrections and improved text phrasing directly within any text box in the browser.

## Features
Real-Time Grammar Checking:

Detects grammatical errors in Arabic text as users type.
Highlights errors with a red underline.
Grammar Suggestions:

Provides suggested corrections in a popup for easy access.
Enhanced Text Editing:

Improves phrasing for better readability and grammatical correctness.
Seamless Integration:

Works in any text area or input field on websites.
How It Works
The extension monitors text input fields in the browser.
When the user types more than 2 characters, the extension sends the text to the Allam LLM grammar-checking model via a locally hosted server.
Allam LLM analyzes the text and returns:
A list of grammar mistakes.
Suggested corrections.
Mistakes are highlighted, and a popup displays suggestions for easy reference.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask with Allam LLM integration)
Extension Framework: Chrome Extensions API
