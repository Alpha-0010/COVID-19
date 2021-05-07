from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
	notification.notify(
		title=title,
		message=message,
		app_icon=None,
		timeout=5
	)

def getdata(url):
	r=requests.get(url)
	return r.text

if __name__ == '__main__':
	# notifyMe('Hello','world')
	while True:
		htmlData=getdata('https://www.mohfw.gov.in/')
		# print(htmlData)
		soup = BeautifulSoup(htmlData, 'html.parser')
		# print(soup.prettify())
		myData=""
		for tr in soup.find_all('tbody')[0].find_all('tr'):
			myData+=tr.get_text()
		myData=myData[1:]
		Itemlist=myData.split("\n\n")

		# print(Itemlist)
		states=['Tamil Nadu']


		for item in Itemlist[0:33]:
			datalist=item.split('\n')
			if datalist[1] in states:
				print(datalist)
				nTitle='Cases of Corona in India'
				nText=f"STATE: {datalist[1]}\n Confirmed Cases: {datalist[2]}\n Cured: {datalist[3]}\n Deaths: {datalist[4]}"
				notifyMe(nTitle,nText)
				time.sleep(2)
		time.sleep(10)
