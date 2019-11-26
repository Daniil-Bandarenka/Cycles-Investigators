from datetime import datetime
from lxml import html

import requests


r = requests.get("http://www.northwest.williams.com/NWP_Portal/CapacityResultsScrollable.action")

html_tree = html.fromstring(r.content)
cycle = html_tree.xpath("//*[*/text()='Cycle:']/following-sibling::td//text()")

print(f"{datetime.now()} : {cycle[0]}")
