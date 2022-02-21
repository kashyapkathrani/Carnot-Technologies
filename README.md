# Problem Statement

Objective: To write a logic block that stores the latest location for all devices in a Redis cache

Data: Refer to the attached excel for raw data of all users. Assume that every entry from excel is one data
point and every data point is received as an input to the function at a time = sts column value. So, while
reading the file, you need to iterate over the entries after sorting the data on the sts column

Problem Statement:
1. Create a local Redis cache server.
2. Read the given excel as per instructions given above
3. Write a code that stores the data of a new excel entry against each device ID
4. Before writing check if the time_stamp value of the new excel entry is greater than the time_stamp
of Redis data. If yes, update the Redis data with new excel data; otherwise, keep the original Redis
data.
5. Now create an API endpoint (in the framework of your choice) that takes device ID and returns
device information in response.
Output: Share entire data stored in Redis cache

# Solution

I have used Django as the framework for developing this Solution. 
### Steps to run the Project:

1. Create an environement and install the required package using requirements.txt file.
    > pip install -r requirements.txt

2. Install and Start local Redis Server

3. Run the Django Application
    > python manage.py runserver


I have used Django REST framework for creating Enpoint.

### The endpoint created is :

1. device/{device_id} : The endpoint returns latest device data by fetching it from Redis Cache.

### Processing the data CSV

To process the CSV file, I have created a function, [processCSV](https://github.com/kashyapkathrani/Carnot-Technologies/blob/master/APIs/utils.py), which runs on start of Django Application and processes the file as follows:

1. Reads the CSV file as Pandas DataFrame
2. Converts timestamp and STS from string to Epoch timestamp format
3. Sorts the DataFrame based on STS
4. For each row, checks whether device data is present in Redis or not
    1. If not, then stores the device data in Redis
    2. If present, Checks if timestamp of new entry is greater than one stored in Redis. If yes, then updating data in redis.




