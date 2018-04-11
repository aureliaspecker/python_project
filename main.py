import os
from flask import Flask, render_template, request

app = Flask("Whatweatherwhere")

@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template("main.html")

@app.route("/events", methods=['GET', 'POST'])
def events():
    secret_key = app.config["SECRET_KEY"]
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    print(request.form['location'])
    playload = {
        "q": "location",
        "units": "metric",
        "appid":config_file["SECRET_KEY"]
    }
#       { data['location'] : 'London',
#       data['keyword'] : 'London',
    return render_template("main.html")

config_file = "config.json"
# The check below is to see if you have the
# config file defined and if you do not, it will display
# basic guidelines steps to set the config file.
if not os.path.isfile(config_file):
    app.logger.error(
        "Your config.json file is missing." +
        "You need to create one in order for this demo app to run." +
        "Please check the README.md file in order to set it up."
    )
else:
    # We are in the case where we have the config file.
    #
    # The line below is the magic statement that is going
    # to load our configuration from the config.json file.
    # After the line below is executed the config defined
    # in config.json will be available in the app variable.
    # Example on how you can get the config values:
    # secret_key = app.secret_key
    # OR
    # secret_key = app.config['SECRET_KEY']
    app.config.from_json(config_file)

app.run(debug=True)
