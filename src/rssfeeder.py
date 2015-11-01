from bs4 import BeautifulSoup
import urllib2
import numpy as np
import string
import time
import feedparser
from lxml import html
import json
import requests
from goose import Goose
reuters = "http://www.reuters.com/tools/rss"



# Function
def getFeedList(url):
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)
	key= []
	val = []

	for td in soup.findAll('td', attrs={'class':'xmlLink'}):
		val.append(td.find('a')['href'])
		key.append(td.find('a').contents[0])

	lower_key = []
	for ii in key:
		lower_key.append(ii.lower())

	index = np.arange(len(val))
	index += 1

	return dict(zip(lower_key, val)), dict(zip(index,key)), key



def RSS_Directory():
	print "Welcome to the RSS Feed Directory"
	time.sleep(0.5) 
	print "..."
	time.sleep(0.5) 
	print "..."
	time.sleep(0.5)  
	print "Here is the list of RSS Feeds available"
	time.sleep(1.0)  

	direct = getFeedList(reuters)
	i = 1
	for ii in direct[2]:
		time.sleep(0.1)
		print "%d) %s" %(i,ii)
		i += 1

	person = input('Select RSS Feed: ')
	#person = 1
	rss_link = getRSS(person, direct)
	link_to_goose = parseRSS(rss_link)
	rss_stories = goose_zipper(link_to_goose)

	return rss_stories


def getRSS(input, dict1):

	tmp1 = dict1[0]
	tmp2 = dict1[1]
	url = ""

	if type(input) is str:
		input = input.lower()
		url = tmp1[input]

	elif type(input) is int:
		new_key = str(tmp2[input])
		key = new_key.lower()
		url = tmp1[key]

	return url 


x = getFeedList(reuters)
y = getRSS(1,x)


def parseRSS(rss_link):
	d = feedparser.parse(rss_link)
	entries = d["entries"]
	tmp = []
	for ii in range(len(entries)):
	  x = entries[ii]
	  tmp.append(x["link"])
	return tmp

def goose_extractor_content(url):
	g = Goose()
	article = g.extract(url=url)
	#article.title ## returns article title
	#article.meta_description ## returns article meta description
	#article.top_image.src ## returns path for main image in article
	#article = g.extract(url=url) ## these scrape full text from article
	return article.cleaned_text

def goose_extractor_title(url):
	g = Goose()
	article = g.extract(url=url)
	#article.title ## returns article title
	#article.meta_description ## returns article meta description
	#article.top_image.src ## returns path for main image in article
	#article = g.extract(url=url) ## these scrape full text from article

	return article.title

def goose_zipper(lst):
	key = []
	val = []
	for ii in lst:
		key.append(goose_extractor_title(ii))

	for jj in lst:
		val.append(goose_extractor_content(ii))

	return dict(zip(key, val))


url = "http://www.reuters.com/article/2015/10/30/us-theatre-knightley-idUSKCN0SO1L920151030?feedType=RSS&feedName=artsNews&utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+news%2Fartsculture+%28Reuters+Arts+%26+Culture+%29"
page = urllib2.urlopen(url2).read()
soup = BeautifulSoup(page)
soup.find("div", {"id": "articleText"})
test1 = feedparser.parse(url2)

z = parseRSS(y)
zz = goose_zipper(z)

