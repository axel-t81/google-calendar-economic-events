# Python file

# 1) Firstly, I need to collect API data

# 2) Then I need to push that to a public Google Calendar

# 3) THen I need to somehow repeat this process every 24 hours, forever


# Okay Step 1 below

## COMMENTS AFTER DAY 1
# The current code is able to get the data for 3 months and print the response as Text
# You can see Earnings Calendar & Python examples and endpoints at https://www.alphavantage.co/documentation/
# What your missing now is:
# (a) Look at the current data and see, as a human, how you could use this in your idea in a practical sense.
# (b) Then you need to turn this text data into something that can be sliced/used for your answer to (a)

## COMMENTS AFTER DAY 2
# The current code is able to get the data for 3 months and print the response as a List, that was originally a CSV download
# The problem today is that there is too much data, and you want to cull things down to the NASDAQ 100 or S&P500 or DowJones, etc
# But you don't know how to access appropriate lines other than using the index value
# But you need something akin to matching the Ticker instead ...and this is the problem you're working on
# You've looked at Filters, Contains(?), Splice, and a few others, inc converting List to Dictionary, but you can't work it out yet

import requests
import json
import csv
import time
import re
import pandas as pd
# This next import statement hides your API Key in another file that should be Ignored by Git
from env import API_KEY

# The API endpoint, You can see Earnings Calendar & Python examples and endpoints at https://www.alphavantage.co/documentation/
CSV_URL = "https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&symbol=IBM&&symbol=AAL&horizon=3month&apikey=API_KEY"

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    print(type(download))
    print(type(decoded_content))
    print(type(cr))
    print(type(df))