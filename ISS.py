import urllib3
import json
import datetime
import time


start = time.time()
# displaying date and time in a regular string format
while True:
    
    if (time.time() > start + 9):
        #collect data from url
        http = urllib3.PoolManager()
        req = http.request('GET', "http://api.open-notify.org/iss-now.json")

        #parse the data into JSON format
        x = req.data.decode("utf-8")
        y = json.loads(x)

        #convert the timestamp from UNIX to regular date and time
        unix_time = y['timestamp'] 
        date_time = datetime.datetime.fromtimestamp(unix_time)
        print("Date & Time:" , date_time.strftime('%Y-%m-%d %H:%M:%S'))

        #display the Latitude and Longitude
        print ("Latitude:", y['iss_position']['latitude'], "Longitude:", y['iss_position']['longitude'])
        start = time.time()

