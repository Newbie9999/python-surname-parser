from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

def getNames(http):
	print("http://vstup.info/2018" + http)
	html = urlopen("http://vstup.info/2018" + http)
	bsObj = BeautifulSoup(html, "lxml")
	nameDivs = bsObj.find("tbody").findAll("tr")
	names = set()
	for n in nameDivs:
		name = n.findAll("td")[1].get_text()
		name = name[0:name.find(" ")]
		names.add(name)
	return names

def getTowns():
	html = urlopen("http://vstup.info")
	bsObj = BeautifulSoup(html, "lxml")
	townLinkContainers = bsObj.find("tbody").findAll("a", href=re.compile("^(/2018/).*$"))
	townLinks = []
	for link in townLinkContainers:
		townLinks.append(link.attrs["href"])
	return townLinks

def getColleges(url):
	html = urlopen("http://vstup.info" + url)
	bsObj = BeautifulSoup(html, "lxml")
	groups = bsObj.findAll("div", {"class":"accordion-group"})
	colLinks = []
	for group in groups:
		links = group.findAll("a", href=re.compile("^(\.\/).*$"))
		for link in links:
			colLinks.append(link.attrs["href"][1:])
	return colLinks

def getPages(url):
	html = urlopen("http://vstup.info/2018" + url)
	bsObj = BeautifulSoup(html, "lxml")
	groups = bsObj.findAll("div", {"class":"accordion-group"})
	groups = groups[1:]
	pageLinks = []
	for group in groups:
		links = group.findAll("a", href=re.compile("^(\.\/).*$"))
		for link in links:
			pageLinks.append(link.attrs["href"][1:])
	return pageLinks

names = set()
towns = getTowns()
colleges = []
i = 0
for town in towns:
	print(town)
	colleges = getColleges(town)
	for college in colleges:
		print(college)
		pages = getPages(college)
		for page in pages:
			print(page)
			names.update(getNames(page))
# print(names)

output = open('surnames.txt', 'w')
for name in names:
	output.write(name + "\n")
output.close()
"""
while len(links)>0:
	print(name.get_text())
	print(len(links), " links")
	url = links[random.randint(0, len(links)-1)].attrs["href"]
	links, name = getLinks(url)
"""