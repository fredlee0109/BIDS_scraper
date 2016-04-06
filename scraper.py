# scraper.py
# @author: Fred Lee
# Intended for BIDS purposes
# Access Token: 462841737254767|2DhTVaex8CEIMjG12myTlJZiKlo

import api
import time
from datetime import datetime

def main():
	
	# print response.json()
	origin = 'https://www.facebook.com/advanotech/timeline?ref=page_internal'
	# print api.fbAPI(origin).point()
	print api.fbAPI(origin).post_date_diff()

	# time.sleep(60)

if __name__ == "__main__":
	main()