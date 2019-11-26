from datetime import datetime
from lxml import html

import requests


r = requests.get("https://tgcmessenger.energytransfer.com/ipost/TGC/capacity/operationally-available-by-location")

html_tree = html.fromstring(r.content)
cycle = html_tree.xpath("//*[@id='cycleDesc']/@value")

print(f"{datetime.now()} : {cycle[0]}")
