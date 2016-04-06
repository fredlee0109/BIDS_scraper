# api.py
# @author: Fred Lee
# Intended for BIDS purposes

import api
import time
import json
# import facebook
import requests
from datetime import datetime
import API_KEY as API_KEY

class fbAPI(object):

	def __init__(self, link):
		start = link.find('facebook.com/') + 13
		if start == -1:
			self.page = None
			return
		if link[start:].find('/') == -1:
			end = 5
		else:
			end = link[start:].find('/') + start
		self.page = link[start:end]
		self.response = requests.get(
			API_KEY.URL.format(
				version=API_KEY.fb_version,
				page=self.page,
				KEY=API_KEY.facebook)
			).json()
		if 'error' in self.response:
			print 'Failed to fetch'

	def point(self):
		if 'error' in self.response:
			print 'Failed to fetch'
			return
		point = 0
		if self.post_date_diff() != None and self.post_date_diff() < 3.154e+7:
			point += 1
			print "date"
		if self.website() != None:
			point += 1
			print "website"
		if self.email() != None:
			point += 1
			print "email"
		if self.description() != None:
			point += 1
			print "description"
		if self.about() != None:
			point += 1
			print "about"
		return point

	def post_date_diff(self):
		if self.page == None:
			return None
		date = datetime.strptime(self.response['posts']['data'][0]['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
		return (datetime.today() - date).total_seconds()

	def website(self):
		if 'website' in self.response:
			return self.response['website']
		return None

	def email(self):
		if 'emails' in self.response:
			return self.response['emails'][0]
		return None

	def description(self):
		if 'description' in self.response:
			return self.response['description']
		return None
	
	def about(self):
		if 'about' in self.response:
			return self.response['about']
		return None

	def id(self):
		return self.response['id']

class twitterAPI(object):

	def __init__(self, link):
		start = link.find('twitter.com/') + 12
		end = link[start:].find('/') + start
		self.page = link[start:end]