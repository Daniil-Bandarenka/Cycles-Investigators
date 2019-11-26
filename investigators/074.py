from datetime import datetime
from lxml import html

import requests


r = requests.get("https://sermessenger.energytransfer.com/ipost/SER/capacity/operationally-available-by-location?max=10")

html_tree = html.fromstring(r.content)
cycle = html_tree.xpath("//*[@id='cycleDesc']/@value")

print(f"{datetime.now()} : {cycle[0]}")
