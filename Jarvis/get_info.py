import sys
import os
import time
import datetime


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
	date.year, date.hour, date.minute)

	return current_date_sentence	


def get_today_weather():
	"""Retrieve weather through OpenWeather"""
	pass

def get_news_headlines():
	""" Retrieve a number of news headlines """
	pass

def get_meetings():
	""" If calendar, enumerate meeting"""
	pass

def get_horoscope():
	""" Give today's horoscope """
	pass

def get_inspirational_quote():
	""" Give an inspirationnal quote """
	pass

def enumerate_lists():
	""" Give the name of every list stored """
	pass

def read_list():
	""" Read a list """
	pass


if __name__ == '__main__':
	print(get_date())
