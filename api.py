# api.py
# @author: Fred Lee
# Intended for BIDS purposes

import api
import time
import json
import facebook
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


	def post_date_diff(self):
		if self.page == None:
			return "No facebook.com detected"
		graph = facebook.GraphAPI(API_KEY.facebook)
		# print graph.get_connections(graph.get_object(self.page)['id'], 'bio')
		# print graph.get_connections(graph.get_object(self.page)['id'], 'posts')
		print graph.get_object(self.page)
		posts = graph.get_connections(self.page, 'posts')
		print '========='
		# print posts
		date = datetime.strptime(posts['data'][0]['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
		return (datetime.today() - date).total_seconds()

class twitterAPI(object):

	def __init__(self, link):
		start = link.find('twitter.com/') + 12
		end = link[start:].find('/') + start
		self.page = link[start:end]