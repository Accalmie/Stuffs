import get_info as g
import user_info as u
import speaker as s
import os
import requests
import json

news_api_key = 'Your key


def print_instruction():
	print("1/ Get the date and time")
	print("2/ Get the weather near you")
	print("3/ Get some news headline")
	print("4/ Quit")
	print("Enter the index of you command :")

def say_headlines(user):

	feeds = user.get_news_feeds()

	feed_count = 1
	for feed in feeds:
		print (str(feed_count) + "/ " + feed[0])
		feed_count += 1

	print ("Which feed would you like to hear ?")

	feed_index = -1
	while (feed_index < 0 or feed_index > feed_count - 1):
		try:
			feed_index = int(raw_input()) - 1
		except ValueError:
			print("Wrong index")

	num = 4
	url = "https://newsapi.org/v1/articles?source=" + feeds[feed_index][1] + "&sortBy=top&apiKey=" + news_api_key
	r = requests.get(url)
	j = json.loads(r.text)
	articles = j['articles']
	feed_pres = "Top articles for : " + feeds[feed_index][0]
	s.say(feed_pres)
	article_count = 0

	for article in articles:
		if article_count >= num:
			break
		else:
			article_title = (str(article_count + 1) + "/ " + article['title'])
			s.say(article_title)
			#print ("URL : " + article['url'])
			article_count += 1


if __name__ == '__main__':

	if os.path.isfile('./main_user.u'):
		main_user = u.load_user()
		
	else:
		main_user = u.register_user()
		u.register_news_feed(main_user)
		u.save_user(main_user)
		print("We registered and saved user " + main_user.name)

	print ("Hello, " + main_user.name)
	print (g.get_date())
	print (g.get_today_weather())
	print("\nHere is an inspirationnal quote to get you started for the day:\n")
	print (g.get_inspirational_quote())
	print("")
	g.get_news_headlines(8, main_user)

	#s.say("Hello, " + main_user.name)
	#s.say(g.get_date())
	#s.say(g.get_today_weather())
	#s.say("Here is an inspirationnal quote to get you started for the day:")
	#s.say(g.get_inspirational_quote())
	#s.say("Have a nice day master :" + main_user.name)


	
	while (True):
		print_instruction()
		command = -1
		while (command < 1 or command > 4):
			try :
				command = int(raw_input())
			except ValueError:
				print("Wrong value")

		if command == 1:
			s.say(g.get_date())
		if command == 2:
			s.say(g.get_today_weather())

		if command == 3:
			say_headlines(main_user)
		
		if command == 4:
			s.say("Goodbye master " + main_user.name)
			break
