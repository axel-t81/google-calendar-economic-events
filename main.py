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

import requests
import json
import csv
import time
# This next import statement hides your API Key in another file that should be Ignored by Git
from env import API_KEY

# The API endpoint, You can see Earnings Calendar & Python examples and endpoints at https://www.alphavantage.co/documentation/
CSV_URL = "https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=API_KEY"

# A GET request to the API. Test if response is successful. If so, Print the response
response = requests.get(CSV_URL)
# Print the status code of the call response
print(response.status_code)
# Print the data you've just called via the GET Request
print(response.text)

### The stuff below is commented out because you can't yet get it to work
#if response.status_code != 200:
#    print("Server didn't return an 'OK' response.  Content was: {!r}".format(response.content))
#else:
#   json_data = response.json()
#   time.sleep(28)
#
#print(json_data)