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
			print 'Not a valid address'
			return
		if link[start:].find('/') == -1:
			end = 5
		else:
			end = link[start:].find('/') + start
		self.page = link[start:end]
		if self.page == 'media':
			print 'Not a page'
			return
		self.response = requests.get(
			API_KEY.URL.format(
				version=API_KEY.fb_version,
				page=self.page,
				KEY=API_KEY.facebook)
			).json()
		if 'error' in self.response:
			print 'Failed to fetch'

	def point(self):
		if 'error' in self.response or self.page == 'media' or self.page == None:
			return
		point = 0
		if self.post_date_diff() != None and self.post_date_diff() < 3.154e+7:
			point += 1
		if self.website() != None:
			point += 1
		if self.email() != None:
			point += 1
		if self.description() != None:
			point += 1
		if self.about() != None:
			point += 1
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

# class twitterAPI(object):

# 	def __init__(self, link):
# 		start = link.find('twitter.com/') + 12
# 		end = link[start:].find('/') + start
# 		self.page = link[start:end]

#  curl --get 'https://api.twitter.com/1.1/statuses/user_timeline.json' --data 'count=1&screen_name=freshy_freddy' --header 'Authorization: OAuth oauth_consumer_key="TvpN2t3xLm1mHlzYUpHtGzN4n", oauth_nonce="0e5bc766548a941a8e3390621d63e1ee", oauth_signature="wbqugutxmpPOLq%2BgTwmQpv4rKPA%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1459930228", oauth_version="1.0"'