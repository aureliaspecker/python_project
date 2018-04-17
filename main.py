import os # imports a library that lets us read the environment variables
import requests
from flask import Flask, render_template, request

app = Flask("Whatweatherwhere")

port = int(os.environ.get("PORT", 5000)) # saved the key as an environment variable

@app.route("/", methods=['GET', 'POST'])
def hello():
    print port #what is this doing?
    return render_template("main.html")

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
    weather = {}
    weather["main"] = response.json()["weather"][0]["main"]
    weather["temp"] = response.json()["main"]["temp"]
    weather["description"] = response.json()["weather"][0]["description"]
    weather["name"] = response.json()["name"]
#       { data['location'] : 'London',
#       data['keyword'] : 'London',

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

    if weather["main"] == "Rain":
        rain_wear = "Take a raincoat and an umbrella!"
        return render_template("weather.html", city_weather=weather, city_wear=rain_wear)
    if weather["main"] == "Thunderstorm":
        thunderstorm_wear = "Make sure your raincoat is water and wind proof!"
        return render_template("weather.html", city_weather=weather, city_wear=thunderstorm_wear)
    if weather["main"] == "Snow":
        snow_wear = "You will need a pair of Moon Boots with hat, scarf and gloves!"
        return render_template("weather.html", city_weather=weather, city_wear=snow_wear)
    if weather["main"] == "Drizzle":
        drizzle_wear = "Today will be humid, so make sure you bring a spare pair of shoes!"
        return render_template("weather.html", city_weather=weather, city_wear=drizzle_wear)
    if weather["main"] == "Clear":
        clear_wear = "It's nice weather - enjoy it while it lasts and wear something summery!"
        return render_template("weather.html", city_weather=weather, city_wear=clear_wear)
    if weather["main"] == "Clouds":
        clouds_wear = "Take a pair of sunglasses just in case the sun comes out!"
        return render_template("weather.html", city_weather=weather, city_wear=clouds_wear)
    if weather["main"] == "Extreme":
        extreme_wear = "Maybe stay at home.."
        return render_template("weather.html", city_weather=weather, city_wear=extreme_wear)
    if weather["main"] == "Additional":
        additional_wear = "insert text"
        return render_template("weather.html", city_weather=weather, city_wear=additional_wear)
    if weather["main"] == "Atmosphere":
        atmosphere_wear = "insert text"
        return render_template("weather.html", city_weather=weather, city_wear=atmosphere_wear)
    else:
        return render_template("events.html", city_weather=weather)


app.run(host='0.0.0.0', port=port, debug=True) # making sure application will start on the specific port
