from run_function_weather_report import *
from datetime import datetime
from paths_owm import *
from Tim_common import *
import time

# **** End of imports **** #

###########################################################################################################
# 
# assign owm_url_weather = 'http://api.openweathermap.org/data/2.5/weather?'
# assign owm_url_forecast = 'http://api.openweathermap.org/data/2.5/forecast?'
# get the OpenWeatherMap api key for queries
#
#
# example of api call to OpenWeatherMap api
# http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={APIKEY}
#
###########################################################################################################
owm_url_weather  = 'http://api.openweathermap.org/data/2.5/weather?'
owm_url_forecast = 'http://api.openweathermap.org/data/2.5/forecast?'
owm_APIKEY = get_open_weather_map_api_key()

# empty list if you want to manually provide cities
city_names_list = []

# comment out below list of cities if you want to manually provide cities
#city_names_list = [('Georgetown', 'TX'), ('Angleton', 'TX'), ('Oak Harbor', 'WA'), ('Wells', 'NV'), \
#                   ('Dublin',     'CA'), ('Hollis',   'NH'), ('Sunnyvale',  'CA')]

if len(city_names_list) == 0:
    clear_screen()
    print('\n')
    city_names_list = get_city_names_for_weather_report(city_names_list)

city_names_list = add_city_object_to_list(city_names_list)

# create file execution_time_path with w+
# remaining writes to this file will be done calling execution_TIME()
f = open(execution_time_path, 'w+')
f.close()

loop_count = 1
while loop_count != 1000:

    # remaining writes to this file will be done calling execution_TIME() 
    # Log start time
    start_time = datetime.now()
    time_message = "TIME: __main__() loop_count = {}  ".format(loop_count)
    execution_TIME(time_message, 'start', start_time)

    # add another carriage return to execution_time_path file.
    f = open(execution_time_path, 'a')
    f.write('\n')
    f.close()

    # __main__() START

    run_weather_report(owm_url_weather, owm_APIKEY, city_names_list)

    # __main__() FINISHED

    # Log finished time
    finished_time = datetime.now()
    time_message = "TIME: __main__() loop_count = {}  ".format(loop_count)
    execution_TIME(time_message, 'finished', start_time, finished_time)

    # add 3 additional carriage return to execution_time_path file.
    # separates loop_counts in file with an extra carriage return (read-ability)
    f = open(execution_time_path, 'a')
    f.write('\n\n\n')
    f.close()

    loop_count += 1