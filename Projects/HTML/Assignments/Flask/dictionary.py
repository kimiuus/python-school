import json
from flask import Flask, request

app = Flask(__name__)

with open("dictionaryfile.json", "r", encoding="utf-8") as file:
    data = json.load(file)

@app.route('/translate/<word>')
def translate(word):
    try:
        response = {
            "English": f"{word}",
            "Finnish": f"{data[word]}",
            }
        return response
    except KeyError:
        response = {
            "error" : "Word not found"
        }
        return response
@app.route("/translate/words/")
def wordlist():
    response = data
    return response
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True)