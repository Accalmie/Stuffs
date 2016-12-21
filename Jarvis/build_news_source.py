import json
import requests

if __name__ == '__main__':

	url = 'https://newsapi.org/v1/sources?language=en'
	r = requests.get(url)
	j = json.loads(r.text)

	sources = j['sources']

	source_list = []

	for source in sources:
		source_list.append(source['id'].encode("utf-8"))

	print(source_list)