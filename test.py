from lxml import html
import requests

url="https://www.linkedin.com/company/10073529?trk=tyah&trkInfo=clickedVertical%3Acompany%2CclickedEntityId%3A10073529%2Cidx%3A1-1-1%2CtarId%3A1461132316737%2Ctas%3Adastrong%20"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = requests.get(url, headers=headers)
tree = html.fromstring(page.content)

print dir(tree)
print tree.text
buyers = tree.xpath('//div[@id="main"]/text()')

print buyers