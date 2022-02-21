import json
import time
import pandas as pd
from django.core.cache import cache
from datetime import datetime

def checkInRedis(row):
    device_id = int(row['device_fk_id'])

    # fetching details from redis by device id
    cache_value = cache.get(device_id)

    # checking if details exists
    if cache_value:
        cache_value = json.loads(cache_value)

        # if timestamp of new entry is greater than one stored in Redis, then updating data in redis
        if row['time_stamp'] > (cache_value['time_stamp']):
            cache.set(device_id, row.to_json())
    else:
        # storing details in Redis for given device id
        cache.set(device_id, row.to_json())

def processCSV():

    # cache.clear()

    start_time = time.time()

    df = pd.read_csv('static/raw_data.csv')
    
    # converting into Epoch Timestamp
    df['time_stamp'] = pd.to_datetime(df['time_stamp']).astype('int64')//10**9
    df['sts'] = pd.to_datetime(df['sts']).astype('int64')//10**9

    # sorting the data by STS 
    df = df.sort_values(by=['sts'])

    # Checking in Redis for each data entry
    df.apply(lambda row : checkInRedis(row), axis = 1)

    print("updated Redis Cache in ", time.time()-start_time)
            
            


