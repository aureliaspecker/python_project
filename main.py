import os # imports a library that lets us read the environment variables
import requests
import twitter
from flask import Flask, render_template, request

app = Flask("Whatweatherwhere")

# saved the weather API key as an environment variable
port = int(os.environ.get("PORT", 5000))

@app.route("/", methods=['GET', 'POST'])
def hello():
    #print port # what is this doing?
    return render_template("main.html") # renders the main page

# Calling the API using the endpoint and secret key.
# Defining a "pay load" which is sent to the API in order for the user to be able to see results based on city name.

@app.route("/weather", methods=['GET', 'POST'])
def events():
    secret_key = os.environ.get("SECRET_KEY")
    endpoint = "http://api.openweathermap.org/data/2.5/weather" # need to update here if we want to change to forecast
    city = request.form['location']
    payload = {
        "q": city,
        "units": "metric",
        "appid": secret_key
    }
    response = requests.get(endpoint, params=payload)
    print response.url
    # "weather" is a dictionary - the responses are the pieces of data we want to use and display within a list the API creates.
    # response.json converts the API string into a list.
    weather = {}
    weather["main"] = response.json()["weather"][0]["main"]
    weather["temp"] = response.json()["main"]["temp"]
    weather["description"] = response.json()["weather"][0]["description"]
    weather["name"] = response.json()["name"]

    api = twitter.Api(
        consumer_key = os.environ.get("consumer_key"),
        consumer_secret = os.environ.get("consumer_secret"),
        access_token_key = os.environ.get("access_token_key"),
        access_token_secret = os.environ.get("access_token_secret")
    )

    print(api.VerifyCredentials())
    {"id": 986265829162483712, "location": "London", "name": "WhatWeatherWear"}

    # AUTOMATIC TWEET WHEN USER SEARCHES
    status = api.PostUpdate("The temperature in {} is {} degrees. #{} #whatweatherwhere".format(weather["name"],weather["temp"],weather["main"]))
    app.logger.info(status.text)

    # List of if statements based on "main" data from the open weather API.
    # Renders weather.html and assigns a css class so we only need to create one css file.
    # We can call the API data and weather tips in our html file using jinja syntax (city_weather and city_wear).
    # Added an else statement if a "main" weather type has not been defined in our if statements.

    if weather["main"] == "Rain":
        rain_wear = "Take a raincoat and an umbrella!"
        return render_template("weather.html", css_class="rain", city_weather=weather, city_wear=rain_wear)
    if weather["main"] == "Thunderstorm":
        thunderstorm_wear = "Make sure your raincoat is water and wind proof!"
        return render_template("weather.html", css_class="thunderstorm", city_weather=weather, city_wear=thunderstorm_wear)
    if weather["main"] == "Snow":
        snow_wear = "You will need a pair of Moon Boots with hat, scarf and gloves!"
        return render_template("weather.html", css_class="snow", city_weather=weather, city_wear=snow_wear)
    if weather["main"] == "Drizzle":
        drizzle_wear = "Today will be humid, so make sure you bring a spare pair of shoes!"
        return render_template("weather.html", css_class="drizzle", city_weather=weather, city_wear=drizzle_wear)
    if weather["main"] == "Clear":
        clear_wear = "It's nice weather - enjoy it while it lasts and wear something summery!"
        return render_template("weather.html", css_class="clear", city_weather=weather, city_wear=clear_wear)
    if weather["main"] == "Clouds":
        clouds_wear = "Take a pair of sunglasses just in case the sun comes out!"
        return render_template("weather.html", css_class="clouds", city_weather=weather, city_wear=clouds_wear)
    if weather["main"] == "Extreme":
        extreme_wear = "Maybe stay at home.."
        return render_template("weather.html", css_class="extreme", city_weather=weather, city_wear=extreme_wear)
    if weather["main"] == "Additional":
        additional_wear = "insert text"
        return render_template("weather.html", css_class="additional", city_weather=weather, city_wear=additional_wear)
    if weather["main"] == "Atmosphere":
        atmosphere_wear = "insert text"
        return render_template("weather.html", css_class="atmosphere", city_weather=weather, city_wear=atmosphere_wear)
    if weather ["main"] == "Haze":
        haze_wear = "insert text"
        return render_template("weather.html", css_class="haze", city_weather=weather, city_wear=haze_wear)
    else:
        return render_template("weather.html", css_class="default", city_weather=weather)

    # Old if statements:
    # if weather["temp"] < 0:
    #     wear = "Wear snow boots!",
    # elif weather["temp"] < 10:
    #     wear = "You may want to bring a coat!"
    # elif weather["temp"] < 20:
    #     wear = "Get your spring shoes out!"
    # elif weather["temp"] < 30:
    #     wear = "Wear some shorts!"
    # else:
    #     wear = "It's hot! Stay at home and have an ice-cream!"
    #
    #
    # return render_template("events.html", city_weather=weather, city_wear=wear)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/whoweare")
def whoweare():
    return render_template("who_we_are.html")

@app.route("/questions")
def questions():
    return render_template("questions.html")


# Making sure application will start on the specific port
app.run(host='0.0.0.0', port=port, debug=True)
