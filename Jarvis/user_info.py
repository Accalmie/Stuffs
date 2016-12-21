import sys
import os
import json
import requests
import pickle


class User:

	def __init__(self, family_name, name, birthday_month, birthday_day, birthday_year):

		self.family_name = family_name
		self.name = name
		self.birthday_month = birthday_month
		self.birthday_day = birthday_day
		self.birthday_year = birthday_year

		self.news_feed = []

	def add_news_feed(self, feed):
		self.news_feed.append(feed)

	def get_news_feeds(self):
		return self.news_feed

def parse_birthday():

	not_done = True

	while (not_done):
		try:
			birthday = raw_input()
			splitted = birthday.split('/')
			birthday_day = int(splitted[0])
			birthday_month = int(splitted[1])
			birthday_year = int(splitted[2])
			not_done = False
		except:
			print "Not a valid birthday date, try again : (format DD/MM/YYYY"

	return birthday_day, birthday_month, birthday_year


def register_user():
	""" Create the user """
	print ("Hello there, what's your name ?")
	name = raw_input()
	print ("Hello " + name + " what is your family name ?")
	family_name = raw_input()
	print("And what is your birthday ? - format : DD/MM/YYYY")
	birthday_day, birthday_month, birthday_year = parse_birthday()

	print ("Welcome " + name + ", I am Jarvis, moving on to the next steps of my setup.")

	user = User(family_name, name, birthday_month, birthday_day, birthday_year)

	return user


def register_news_feed(user):
	print("Now we are going to register some news feeds to keep you updated with the world")
	print("This is the list of the current available sources :")

	source_list = get_sources_list()
	source_list_to_string(source_list)

	while (True):
		print("Please enter the index of a news feed you want to add to your list")
		print("Enter 99 to re-print the list and 0 when done")


		not_done = True

		while(not_done):
			try:
				asked = int(raw_input())
				not_done = False
			except ValueError:
				print("Not a number !")
				print("Please enter the index of a news feed you want to add to your list")
				print("Enter 99 to re-print the list and 0 when done")


		if asked == 0:
			break
		elif asked == 99:
			source_list_to_string(source_list)
		elif asked < len(source_list):
			user.add_news_feed(source_list[asked - 1])
			print("Added : " + source_list[asked - 1][0])
		else:
			print ("Wrong Index")
	#print(format_list)



def get_sources_list():
	"""Fetches source list from the news api"""
	url = 'https://newsapi.org/v1/sources?language=en'
	r = requests.get(url)
	j = json.loads(r.text)

	sources = j['sources']

	source_list = []

	for source in sources:
		source_list.append([source['name'].encode("utf-8"), source['id'].encode("utf-8")])

	return source_list

def source_list_to_string(source_list):

	for i in range (1, len(source_list)):
		print (str(i) + ") " + source_list[i - 1][0])


def save_user(user):
	try:
		save = open('main_user.u', 'wb')
		pickle.dump(user, save)
	except IOError:
		print ("Couldn't save user file")

def load_user():
	try:
		file = open('main_user.u', 'rb')
		user = pickle.load(file)
		#print("Done")
		return user
	except IOError:
		print("Couldn't load user")


if __name__ == '__main__':
	if os.path.isfile('./main_user.u'):
		main_user = load_user()
		print(main_user.news_feed)
	else:
		main_user = register_user()
		#print("We registered user " + main_user.name)
		register_news_feed(main_user)
		#print(main_user.news_feed)
		save_user(main_user)

