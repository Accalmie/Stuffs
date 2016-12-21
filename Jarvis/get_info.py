import sys
import os
import time
import datetime
import requests
import json
import forecastio
import user_info as u 
from gtts import gTTS
import speaker as s

forecast_api_key = '9b4e7369ae70106a95cad017901e4afb'
news_api_key = '4063190606a643f99106404030de7fd7'


def get_month_from_number(num):
	switch = {
	    1 : "January",
	    2 : "February",
	    3 : "March",
	    4 : "April",
	    5 : "May",
	    6 : "June",
	    7 : "July",
	    8 : "August",
	    9 : "September",
	    10 : "October",
	    11 : "November",
	    12 : "December"
	}
	return switch.get(num, "Not found")

def get_date():
	"""Retrieve current date"""
	""" TODO : GET PROPER DATE FOR DAY """

	date = datetime.datetime.now()

	current_date_sentence = 'Today, we are the {} of {} {} and it is {} {}'.format(date.day, get_month_from_number(date.month), 
	date.year, date.hour % 12, date.minute)

	return current_date_sentence	

def get_localisation():
	url = 'http://freegeoip.net/json'
	r = requests.get(url)
	j = json.loads(r.text)
	lat = j['latitude']
	lon = j['longitude']
	city = j['city']

	return lat, lon, city

def get_today_weather():
	"""Retrieve weather through DarkSky API"""
	lat, lon, city = get_localisation()

	forecast = forecastio.load_forecast(forecast_api_key, lat, lon)

	now = forecast.currently()
	weather_sentence = "It is " + now.summary + " near " + city + ", and the temperature is " + str(now.temperature) + " degrees."

	return weather_sentence


def get_news_headlines(num, user):
	""" Retrieve a number of news headlines """

	feeds = user.get_news_feeds()

	for feed in feeds:
		url = "https://newsapi.org/v1/articles?source=" + feed[1] + "&sortBy=top&apiKey=" + news_api_key
		r = requests.get(url)
		j = json.loads(r.text)
		articles = j['articles']
		print ("Top articles for : " + feed[0])
		article_count = 0

		for article in articles:
			if article_count >= num:
				break
			else:
				print (str(article_count + 1) + "/ " + article['title'])
				#print ("URL : " + article['url'])
				article_count += 1

		print("")

	print("Done retrieving articles")


def get_meetings():
	""" If calendar, enumerate meeting"""
	pass

def get_horoscope():
	""" Give today's horoscope """

def get_inspirational_quote():
	""" Give an inspirationnal quote """
	url = "http://quotes.rest/qod.json"
	r = requests.get(url)
	j = json.loads(r.text)

	try:
		quote = j['contents']['quotes'][0]['quote']
		author = j['contents']['quotes'][0]['author']

		quote_sentence = quote + "\n" + "by " + author

	except KeyError:
		quote_sentence = "Stand aside, and try not to catch fire if I shed sparks of genius."

	return quote_sentence


def enumerate_lists():
	""" Give the name of every list stored """
	pass

def read_list():
	""" Read a list """
	pass


if __name__ == '__main__':
	
	if os.path.isfile('./main_user.u'):
		main_user = u.load_user()
		
	else:
		main_user = u.register_user()
		u.register_news_feed(main_user)
		u.save_user(main_user)
		print("We registered and saved user " + main_user.name)

	print ("Hello, " + main_user.name)
	print (get_date())
	print (get_today_weather())
	print("\nHere is an inspirationnal quote to get you started for the day:\n")
	print (get_inspirational_quote())
	print("")
	get_news_headlines(8, main_user)

	s.say("Hello, " + main_user.name)
	s.say(get_date())
	s.say(get_today_weather())
	s.say("Here is an inspirationnal quote to get you started for the day:")
	s.say(get_inspirational_quote())
	s.say("Have a nice day master :" + main_user.name)

	


