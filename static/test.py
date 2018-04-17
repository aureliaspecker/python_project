import twitter

api = twitter.Api(consumer_key='nZaBDWJQJ4V2iBfjkosROsBS7',
                      consumer_secret='XGzOKAebDPZeEP96zPbqExmzYghpxVmpRTBzaSvrnXZzafy6c9',
                      access_token_key='986265829162483712-Q4YqfeGHoJDbp97IiIHZen2Ib6Qhgz0',
                      access_token_secret='DTGVmQWjzEvgq6A8902UPJmYiN1MLZA7qN8HWcwF9bYzI')

print(api.VerifyCredentials())
{"id": 986265829162483712, "location": "London", "name": "WhatWeatherWear"}

# TO TWEET - ADD TEXT
status = api.PostUpdate('What the weather is, where you are, and what to wear! #WhatWeatherWear')
print(status.text)


# TO GET TWEETS FROM USER (in this case What Weather Wear)
#def getTweets():
#	x = t.statuses.home_timeline(screen_name="WhatWeatherWear")
#	return x
#	print x

# TO DISPLAY A NUMBER OR NEW TWEETS AND USERNAMES
#def showTweets(x, num):
#    for i in range(0, num):
#        line1 = (x[i]['user']['screen_name'])
#        line2 = (x[i]['text'])
#       w = Label(master, text=line1 + "\n" + line2 + "\n\n")
#        w.pack()


#numberOfTweets = 5        