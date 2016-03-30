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
		start = link.index('facebook.com/') + 13
		end = link[start:].find('/') + start
		self.page = link[start:end]


	def post_date_diff(self):
		graph = facebook.GraphAPI(API_KEY.key)
		posts = graph.get_connections(self.page, 'posts')
		date = datetime.strptime(posts['data'][0]['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
		print (datetime.today() - date).total_seconds()
