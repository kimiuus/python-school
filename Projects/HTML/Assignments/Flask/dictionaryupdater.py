import json
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def wordAdd():

    if request.method == "POST":

        engword = request.form.get("eng")
        finword = request.form.get("fin")
        with open("dictionaryfile.json", "r+") as file:
            data = json.load(file)
            data[engword] = finword
            file.seek(0)
            json.dump(data, file, indent=4)
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)