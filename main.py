from flask import Flask, render_template, request

app = Flask("Whatweatherwhere")

@app.route("/", methods=['GET', 'POST'])
def hello():

    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    print(request)
    return render_template("main.html")

@app.route("/events", methods=['GET', 'POST'])
def events():
    print(request.form['location'])

        playload = {}

#       { data['location'] : 'London',
#       data['keyword'] : 'London',

    return render_template("main.html", data)

app.run(debug=True)
