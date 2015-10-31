from flask import Flask
from flask import render_template
from flask import request
from flask import json
from urllib import urlopen
app = Flask(__name__)

url = "https://api.edamam.com/search?q=chicken&app_id=a8c883e0&app_key=2e7eb13027fc74be1b6e9b022e53c207"
url2 = "https://api.edamam.com/search?q={0},{1},{2},{3}&app_id=a8c883e0&app_key=2e7eb13027fc74be1b6e9b022e53c207"

@app.route('/')
def index():

    return render_template("index.html")

# @app.route('/url/<items>')
# def hello_world(items):
#     # return urlopen(url.format(first, last)).read()
#     url2 = "https://api.edamam.com/search?q="
#     #chicken
#     url3 = "&app_id=a8c883e0&app_key=2e7eb13027fc74be1b6e9b022e53c207"
#     return urlopen(url2 + items + url3).read()
#     # return render_template("index.html");

@app.route('/handle_form', methods=['POST'])
def handle_data():
    a = request.form["a"]
    b = request.form["b"]
    c = request.form["c"]
    d = request.form["d"]
    jsonData = urlopen(url2.format(a, b, c, d)).read()
    #return jsonData
    return render_template("results.html", jsonData=json.dumps(jsonData))

    #your code
if __name__ == '__main__':
    app.run(debug=True)