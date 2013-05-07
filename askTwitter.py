import urllib
import json

keyword = raw_input("Enter a search keyword for twitter:")
num_results = int(raw_input("How many pages of results do you want?"))

for i in range(num_results):	
	destination = "http://search.twitter.com/search.json?q=%s&page=%s" % (keyword, num_results)
	response = urllib.urlopen(destination)
	jsonResponse = json.load(response)
	results = jsonResponse['results']
	for next in results:
		text = next['text']
		print text
