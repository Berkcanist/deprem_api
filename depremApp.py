import requests
import time
import json
url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"

payload = {}
headers = {}

while(1):
	response = requests.request("GET", url)
	result = json.loads(response.text)

	count = 0
	print("{:<24} {:<39}  {:<12} {:<12}".format("Tarih", "Bölge", "Büyüklük", "Derinlik"))

	for i in result["result"]:
		if count > 10:
			break
		if i["mag"] >= 4:
			print("{:<24} {:<39}  {:<12} {:<12}".format(i["date"], i["title"], i["mag"], i["depth"]))
			count += 1
	print(" ")
	time.sleep(5)

