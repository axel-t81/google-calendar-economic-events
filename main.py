# Python file
# * Need to put up guarded function to run main
# * Need to collect API data
# * But this CSV data is 9000+ rows long
# * So need to work out a way to curate this
# * Then this curated data needs to sent to an ICS file
# * ANd the user will need to collect all of them, or have a way to select which ones they want
# * This process needs to be repeated, whenever a user accesses the script; on demand.

import requests
import csv
import ssl

# This next import statement hides your API Key in another file that should be Ignored by Git
from env import API_KEY

# The API endpoint, You can see Earnings Calendar & Python examples and endpoints at https://www.alphavantage.co/documentation/
csv_url = "https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=API_KEY"

# Ignore SSL certificate errors
# Remove this section, and remove context=ctx if I get errors with https sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

my_list = []

with requests.Session() as phone:
    download = phone.get(csv_url)
    print(type(download))
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    print(type(cr))
    my_list = list(cr) # This works in putting all data in a List
    print(my_list) # And you can print out this massive list
    my_dict = dict(cr) # I tried to replicate this ...but with a Dictionary
    print(type(my_dict)) 
    print(my_dict) # But nothing is appended to the dictionary
