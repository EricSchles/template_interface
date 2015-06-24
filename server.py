from flask import Flask, render_template, request
from subprocess import call
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        option = request.form.get("option_list")
        option = option.split(" ")
        call(option)
    return render_template("index.html")

app.run(debug=True)
