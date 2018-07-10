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

# This is in place for a future enhancement
owm_url_forecast = 'http://api.openweathermap.org/data/2.5/forecast?'

owm_APIKEY = get_open_weather_map_api_key()

# empty list if you want to manually provide cities
city_names_list = []

# an option, create a list of cities to track in weather and forecast report
# if this option is chosen, then get_city_names_for_weather_report(city_names_list) will NOT be called
#
# if this option is not chosen, remove the list below or comment the list assignment out.
#
# if you are tracking cities outside of the USA, you will need to enter the long name of the country.
#
# if you are tracking cities inside the USA, you will enter the abbreviation of the state.
city_names_list = [('Georgetown', 'TX'), ('Oak Harbor', 'WA'), ('New York', 'NY'), ('London', 'England')]

# if city_names_list is an empty list call get_city_names_for_weather_report(city_names_list)
# - user will have to enter each city and country or state to be tracked
if len(city_names_list) == 0:
    clear_screen()
    city_names_list = get_city_names_for_weather_report(city_names_list)

# now that all cities to be tracked are known, pass in city_names_list to create_city_object_list(city_names_list).
# the return will be a list of city instances (one for each city being tracked) of the class CITY().
#
# city_names_list will no longer be used.
# city_object_list will be used after this call is done.
city_object_list = create_city_object_list(city_names_list)

# get_city_coordinates() will update city instances with
# geocode lat and lng
# owm city id
get_city_coordinates(city_object_list)


loop_count = 1

# while loop determines number of times to run the reports
while loop_count != 1000:

    # __main__() START

    # run_report with report = 'weather')
    # run_report with report = 'forecast')
    run_report(owm_url_weather, owm_url_forecast, owm_APIKEY, city_object_list, report = 'weather')
    run_report(owm_url_weather, owm_url_forecast, owm_APIKEY, city_object_list, report = 'forecast')

    # __main__() FINISHED

    loop_count += 1