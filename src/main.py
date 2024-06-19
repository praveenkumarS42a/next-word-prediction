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
    app.run(debug=True)

