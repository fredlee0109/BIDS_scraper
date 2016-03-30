# scraper.py
# @author: Fred Lee
# Intended for BIDS purposes
# Access Token: 462841737254767|2DhTVaex8CEIMjG12myTlJZiKlo

import api
import time
import json
from datetime import datetime

def main():
	origin = 'https://www.facebook.com/advanotech/timeline?ref=page_internal'
	api.fbAPI(origin).post_date_diff()

	# time.sleep(60)

if __name__ == "__main__":
	main()