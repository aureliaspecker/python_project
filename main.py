from flask import Flask, render_template, request

app = Flask("Whatweatherwhere")

@app.route("/")
def hello():
    return render_template("main.html")

app.run(debug=True)
