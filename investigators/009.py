from datetime import datetime
from lxml import html

import requests

try:
    r = requests.get("https://peplmessenger.energytransfer.com/ipost/PEPL/capacity/operationally-available-by-location")

    html_tree = html.fromstring(r.content)
    cycle = html_tree.xpath("//*[@id='cycleDesc']/@value")
    post_datetime = html_tree.xpath("//*[text()='Post Date/Time:']/following-sibling::text()")

    print(f"{datetime.now()},{cycle[0]},{post_datetime[0].strip()}")
except Exception as e:
    print(f"{datetime.now()},{str(e)},0")
