import os
from flask import Flask, render_template, request, jsonify
from spellchecker_module import SpellCheckerModule

app = Flask(__name__)
spellchecker = SpellCheckerModule()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct():
    data = request.json
    text = data['text']
    corrected_text = spellchecker.check_sentence(text)
    return jsonify({'corrected_text': corrected_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the port dynamically (Render will assign a port)
    app.run(host='0.0.0.0', port=port, debug=True)
