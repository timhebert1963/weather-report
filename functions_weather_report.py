from modules_weather_report import *
from Tim_common import *
from paths_owm import *
from datetime import datetime
from colorama import Fore, Back, Style, init
init(autoreset = True)

import sys
import time
import requests
import json
import os
import googlemaps

# **** End of imports **** #


def welcome_banner():

    # number of characters in each line. some characters can be a blank space.
    line_len = 118

    # assign string to display in display_banner()
    first_string  = "Welcome to the Weather and Forecast Report"
    second_string = "Weather Report: Current Weather, Temperature, Wind and Visibility"
    third_string  = "Forecast Report: Three day Forecast of Temperatures and Weather Conditions"
    fourth_string = "OpenWeatherMap url: http://api.openweathermap.org/data/2.5/weather? used for queries"

    first_string  = pad_banner_string(first_string, line_len)
    second_string = pad_banner_string(second_string, line_len)
    third_string  = pad_banner_string(third_string, line_len)
    fourth_string = pad_banner_string(fourth_string, line_len)

    print(first_string)
    print('\n')
    print(second_string)
    print('\n')
    print(third_string)
    print('\n')
    print(fourth_string)
    print('\n')
    print('\n')

# **** End of welcome_to_stock_quotes_banner() **** #


def weather_report_banner():

    # number of characters in each line. some characters can be a blank space.
    line_len = 118

    # assign string to display in display_banner()
    first_string  = "The Weather Report"
    second_string = "Current Weather, Temperature, Wind and Visibility"
    third_string  = "OpenWeatherMap url: http://api.openweathermap.org/data/2.5/weather? used for queries"

    first_string  = pad_banner_string(first_string, line_len)
    second_string = pad_banner_string(second_string, line_len)
    third_string  = pad_banner_string(third_string, line_len)

    print(first_string)
    print('\n')
    print(second_string)
    print('\n')
    print(third_string)
    print('\n')

# **** End of weather_report_banner() **** #


def gather_current_weather_data_banner():

    # number of characters in each line. some characters can be a blank space.
    line_len = 118

    # assign string to display in display_banner()
    first_string  = "Collecting Current Weather Data"
    second_string = "Preparing for Forecast Report"
    third_string  = "OpenWeatherMap url: http://api.openweathermap.org/data/2.5/weather? used for queries"

    first_string  = pad_banner_string(first_string, line_len)
    second_string = pad_banner_string(second_string, line_len)
    third_string  = pad_banner_string(third_string, line_len)

    print(first_string)
    print('\n')
    print(second_string)
    print('\n')
    print(third_string)
    print('\n')

# **** End of forecast_report_banner() **** #


def forecast_report_banner():

    # number of characters in each line. some characters can be a blank space.
    line_len = 118

    # assign string to display in display_banner()
    first_string  = "The Forecast Report"
    second_string = "Three day Forecast of Temperatures and Weather Conditions"
    third_string  = "OpenWeatherMap url: http://api.openweathermap.org/data/2.5/forecast? used for queries"

    first_string  = pad_banner_string(first_string, line_len)
    second_string = pad_banner_string(second_string, line_len)
    third_string  = pad_banner_string(third_string, line_len)

    print(first_string)
    print('\n')
    print(second_string)
    print('\n')
    print(third_string)
    print('\n')

# **** End of forecast_report_banner() **** #


def thank_you_banner():

    # number of characters in each line. some characters can be a blank space.
    line_len = 118

    # assign string to display in display_banner()
    first_string  = "####################################################"
    second_string = "#                                                  #"
    third_string  = "#      Thank You for using The Weather Report      #"
    fourth_string = "#                                                  #"
    fifth_string  = "####################################################"

    first_string  = pad_banner_string(first_string, line_len)
    second_string = pad_banner_string(second_string, line_len)
    third_string  = pad_banner_string(third_string, line_len)
    fourth_string = pad_banner_string(fourth_string, line_len)
    fifth_string  = pad_banner_string(fifth_string, line_len)

    print(first_string)
    print(second_string)
    print(third_string)
    print(fourth_string)
    print(fifth_string)
    print('\n')
    print('\n')

# **** End of thank_you_banner() **** #


def pad_banner_string(string, line_len):

    # create spaces for front and back of first_string for display
    string_front = int((line_len - len(string)) / 2)
    string_back  = line_len - (string_front + len(string))

    front = ''
    back  = ''

    for i in range(string_front + 1):
        front = front + " "

    for i in range(string_back + 1):
        back = back + " "

    string = front + string + back

    return string

# **** End of function pad_banner_string() **** #


def get_open_weather_map_api_key():

    # open file owm_apikey_path
    # readline 2 (which is actually line 3)
    # return key
    api_key = open(owm_apikey_path,'r')
    lines   = api_key.readlines()
    api_key.close()
    key     = lines[2][:-1]

    return key

# **** End of get_open_weather_map_api_key() **** #


def get_city_names_for_weather_report(city_names_list):
    
    def enter_country_or_state():

        # enter_country_or_state() will ask user for the country long name or the USA state abbreviated name

        valid_string = True

        while valid_string == True:

            print('\n')
            print(" If the city is in the USA provide an abbreviated state name.")
            print(" If the city is outside the USA provide a long name for the country.")
            print('\n')
            country_or_state = input(" Please enter the country or the state for the city of {}:  ".format(city_name))
            print('\n')

            # check for len(city) == 0
            # user pressed 'Enter' and did not input a string
            if len(country_or_state) == 0:
                clear_screen()
                time.sleep(.5)
                print(" A country or state name was not entered. Please Try Again.")

            else:
                valid_string = False
                return country_or_state

    # **** End of function enter_more_city_names() **** #


    def enter_more_city_names():

        # find out if user would like to enter more cities to track in the reports

        is_answer_valid = False

        clear_screen()

        while not is_answer_valid:
            answer = input(" Do you want to add another city to the Weather Report? 'y' or 'n'  ")

            if answer.lower() == 'y' or answer.lower() == 'yes' or answer.lower() == 'n' or answer.lower() == 'no':
                return answer
            else:
                print(" You did not enter 'y' or 'n'. Please Try Again.")

    # **** End of function enter_more_city_names() **** #

    enter_city_names = True

    while enter_city_names == True:

        #print('\n')
        city_name = input(" Enter the city name for the Weather Report:  ").title()

        # check for len(city) == 0
        # user pressed 'Enter' and did not input a string
        if len(city_name) == 0:
            clear_screen()
            time.sleep(.5)
            print(" A city name was not entered. Please Try Again.")

        else:

            country_or_state = enter_country_or_state()

            # check to ensure user entered a valid city, country_or_state
            # does_city_exist() will return True or False
            result = geocode_db_does_city_exist(city_name, country_or_state)

            # need to add geocode_db check on result
            # need to add owm_db check on result
            if result == True:
                result = owm_db_does_city_exist(city_name, country_or_state)

            if not result:
                print(" A valid city name was not entered. Please Try Again, and enter a valid city")

            else:
                city_names_list.append((city_name, country_or_state))
                answer = enter_more_city_names()

                if answer.lower() != 'y' and answer.lower()!= 'yes':

                    return city_names_list

                else:
                    pass     # more city, country_or_state names will be added to the city_names_list

# **** End of function get_city_names_for_weather_report() **** #


def geocode_db_does_city_exist(city_name, country_or_state):

    ###########################################################################################################
    #
    # geocode_db_does_city_exist() will determine if the city, country_or_state are valid
    # - need to loop through the [0]['address_components'][index_num]['long_name']
    #
    ###########################################################################################################

    # api_key for googlemaps geocode api
    geocode_api_key = os.environ['APIKEY']

    # start googlemaps Client
    gm = googlemaps.Client(key=geocode_api_key)

    try:
        # protection against an invalid name. Prevent a crash gm.geocode key does not exist

        for i in range(len(gm.geocode((city_name, country_or_state))[0]['address_components'])):

            try:
                # get the long_name from geocode
                name = gm.geocode((city_name, country_or_state))[0]['address_components'][i]['long_name']

                # compare the city name and name from geocode
                # if true then return True
                if city_name.lower() == name.lower():

                    return True

            except Exception as message:
                # catch exception messages and pass
                pass

    except:
        pass

    # if no match return False
    return False

# **** End of function geocode_db_does_city_exist() **** #


def owm_db_does_city_exist(city_name, country_or_state):

    ###########################################################################################################
    #
    # owm_db_does_city_exist() will determine if the city, country_or_state are valid
    # - need to loop through the [index_num]['name']
    #
    ###########################################################################################################

    # open and read the file city.list.json which has the city_id
    # owm_city_list_json_path is imported - from paths_owm import *
    open_file = open(owm_city_list_json_path + 'city.list.json', 'r', encoding='utf-8')
    read_file = json.loads(open_file.read())
    open_file.close()

    # loop through the read_file and assign owm_name
    # if owm_name == city:
    #     check to see if int(geocode_lat) == int(owm_lat) and int(geocode_lng) == int(owm_lon)
    #     if this is true then assign city_id to   
    for i in range(len(read_file)):
        owm_name = read_file[i]['name']

        if owm_name.lower() == city_name.lower():

            return True

    try:

        # A customized file "may" exist for city, country entries not available in city.list.json
        open_file = open(owm_city_list_json_path + 'customized.city.list.json', 'r', encoding='utf-8')
        custom_file = json.loads(open_file.read())
        open_file.close()

        for i in range(len(custom_file)):

            owm_name = custom_file[i]['name']

            if owm_name.lower() == city_name.lower():

                return True

    except:
        pass

    # if owm_name.lower() == city.city_name.lower() did not find a match
    # return False
    return False

# **** End of function owm_db_does_city_exist() **** #


def create_city_object_list(city_names_list):

    # this function will create a city_object_list
    # - create an instance of the class City()
    # - assign city_name to city_object.city_name
    # - assign country_or_state to city_object.country_or_state

    city_object_list = []

    for i in range(len(city_names_list)):
        city_name = city_names_list[i][0].title()
        country_or_state = city_names_list[i][1].upper()

        city_object = City()
        city_object.city_name = city_name
        city_object.country_or_state = country_or_state
        city_object_list.append(city_object)

    return city_object_list

# **** End of function create_city_object_list() **** #


def get_geocode_degrees(city_object_list, pb):

    # get the geocode latitude and longitude for each city
    
    # api_key for googlemaps geocode api
    geocode_api_key = os.environ['APIKEY']
    
    # start googlemaps Client
    gm = googlemaps.Client(key=geocode_api_key)

    # call display_progress_bar_query_type to display query type
    display_progress_bar_query_type('geocode')

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    for city in city_object_list:

        if city.geocode_degrees == False:

            # assign item = (city, country_or_state)
            item = (city.city_name, city.country_or_state)

            try:
                # call the geocode api
                # get the geocode lat and lng 
                # lat and lng are returned from api as 'str'. assigning as float
                # need to compare to owm_lat and lon in other functions. better to assign as float now
                city.geocode_lat = float(gm.geocode(item)[0]['geometry']['location']['lat'])
                city.geocode_lng = float(gm.geocode(item)[0]['geometry']['location']['lng'])

                # geocode degrees are now updated in city_obect
                # assign city.geocode_degrees = True
                city.geocode_degrees = True

            except:
                # it is possible the city is not valid or cannot be found in the geocode query
                # assign the lat, lng values to 'NA'
                # hopefully this does not happen
                city.geocode_lat = 'NA'
                city.geocode_lng = 'NA'

        # progress bar for query
        pb.query_complete += 1

        display_progress_bar(pb)
        time.sleep(.1)

# **** End of function get_geocode_degrees() **** #


def get_city_id(city_object_list, pb):

    ###########################################################################################################
    #
    # Need to pass City ID to OpenWeatherMap api for accuracy
    # - match the geocode lat and lon with the OpenWeatherMap lat and lon
    # - when the match occurs then extract the city_id out of the OpenWeatherMap json dictionary
    #
    ###########################################################################################################

    # open and read the file city.list.json which has the city_id
    # owm_city_list_json_path is imported - from paths_owm import *
    open_file = open(owm_city_list_json_path + 'city.list.json', 'r', encoding='utf-8')
    read_file = json.loads(open_file.read())
    open_file.close()

    # call display_progress_bar_query_type to display query type
    display_progress_bar_query_type('city_id')

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    for city in city_object_list:

        # if city.owm_city_id == 0 then update city.owm_city_id = owm_city_id
        # else: city.owm_city_id already has valid city_id assigned -> do nothing 
        if city.owm_city_id == 0:

            # loop through the read_file and assign owm_name
            # if owm_name == city:
            #     check to see if int(geocode_lat) == int(owm_lat) and int(geocode_lng) == int(owm_lon)
            #     if this is true then assign city_id to city.owm_city_id
            # assign city_id_found = False - may need to do a lookup in customized.city.list.json
            # if city is not found in city.list.json.
            city_id_found = False  
            for i in range(len(read_file)):
                try:
                    owm_name = read_file[i]['name']
                except:
                    print("FATAL ERROR: get_city_id() {} does not exist in city.list.json file")
                    print("Pause # *********************** #")
                    print("PAUSE # *******  VERIFY  ****** #")
                    input("Pause # *********************** #")

                if owm_name.lower() == city.city_name.lower():

                    owm_city_id = read_file[i]['id']
                    owm_lat     = read_file[i]['coord']['lat']
                    owm_lon     = read_file[i]['coord']['lon']

                    # check to see if int(lat) and int(lon) are within a range of +2 or -2 for lat and lon
                    # when comparing geocode and OpenWeatherMap coordinates. if this is True there is a match
                    #
                    # the coordinates between geocode and OpenWeatherMap are not always exactly the same but should
                    # be within a tolerance of +2 or -2
                    if (int(city.geocode_lat) <= int(owm_lat + 2) and int(city.geocode_lat) >= int(owm_lat - 2)) and \
                       (int(city.geocode_lng) <= int(owm_lon + 2) and int(city.geocode_lng) >= int(owm_lon - 2)):

                        city.owm_city_id = owm_city_id
                        city_id_found = True

                        break

            # if city_id not found in city.list.json then try the custom.city.list.json file.
            if city_id_found == False:
                open_file = open(owm_city_list_json_path + 'customized.city.list.json', 'r', encoding='utf-8')
                custom_file = json.loads(open_file.read())
                open_file.close()

                for i in range(len(custom_file)):
                    try:
                        owm_name = custom_file[i]['name']
                    except:
                        print("FATAL ERROR: get_city_id() {} does not exist in city.list.json file")
                        print("Pause # *********************** #")
                        print("PAUSE # *******  VERIFY  ****** #")
                        input("Pause # *********************** #")

                    if owm_name.lower() == city.city_name.lower():

                        owm_city_id = custom_file[i]['id']
                        owm_lat     = custom_file[i]['coord']['lat']
                        owm_lon     = custom_file[i]['coord']['lon']

                        # check to see if int(lat) and int(lon) are within a range of +2 or -2 for lat and lon
                        # when comparing geocode and OpenWeatherMap coordinates. if this is True there is a match
                        #
                        # the coordinates between geocode and OpenWeatherMap are not always exactly the same but should
                        # be within a tolerance of +2 or -2
                        if (int(city.geocode_lat) <= int(owm_lat + 2) and int(city.geocode_lat) >= int(owm_lat - 2)) and \
                           (int(city.geocode_lng) <= int(owm_lon + 2) and int(city.geocode_lng) >= int(owm_lon - 2)):

                            city.owm_city_id = owm_city_id
                            city_id_found = True

                            break

        # progress bar for query progress
        pb.query_complete += 1

        display_progress_bar(pb)
        time.sleep(.1)

# **** End of function get_city_id() **** #


def setup_local_tz_attributes(city_object_list):

    # setup_local_tz_attributes() will update the city instance attributes
    # city instance attribute local_timeone
    # city instance attribute local_tz_dt_txt
    # city instance attribute local_weekday_name
    for city in city_object_list:
        city.update_local_timezone()
        city.update_local_tz_dt_txt()
        city.update_local_weekday_name()

# **** End of function setup_local_tz_attributes() **** #


def setup_forecast_attributes(city_object_list):

    # setup_forecast_attributes() will assign forecast attributes to the values of weather attributes
    # this is setting up for the forecast report
    for city in city_object_list:

        # updating the city instance attributes
        # self.<weekday name>_weather_code = self.owm_weather_code
        # self.<weekday name>_high_temp    = self.owm_temp
        # self.<weekday name>_weather_description = self.owm_description
        city.update_first_weather_code()
        city.update_first_high_temp()
        city.update_first_description()

# **** End of function setup_forecast_attributes() **** #


def ensure_weather_report_is_run(city_object_list, owm_url_weather, owm_APIKEY):

    # ensure_weather_report_is_run() will verify that weather report has been run for each city instance
    # if city.owm_weather_report_run == True the weather report has been run
    # if city.owm_weather_report_run == False the weather report has not been run
    # - run the weather report
    #
    # the 1st city instance needs to be checked. weather report is not run for single instances.
    city = city_object_list[0]
    if city.owm_weather_report_run == False or city.perform_owm_weather_api_query() == True:

        # display banner
        clear_screen()
        time.sleep(.5)
        print('\n')

        gather_current_weather_data_banner()

        # display progress bar scale
        pb = ProgressBar(len(city_object_list))
        progress_bar_scale()

        # get the current weather data for each city
        get_owm_weather_data(city_object_list, owm_url_weather, owm_APIKEY, pb)

        # assign pb.query_complete = 0
        #   - need to assign to 0 now that query is complete
        #   - this will allow Progress Bar to start at 0% for the next "new" query.
        pb.query_complete = 0

        # assign the weather data to city instances
        setup_weather_report(city_object_list)

        # assign the timezone attributes
        setup_local_tz_attributes(city_object_list)

        # move the current weather data to forecast attributes for the 1st day
        setup_forecast_attributes(city_object_list)

        clear_screen()
        time.sleep(.5)
        print('\n')

# **** End of function ensure_weather_report_is_run() **** #


def get_owm_weather_data(city_object_list, owm_url_weather, owm_APIKEY, pb):

    def write_wrf_json(data, city_name, country_or_state):

        # owm = 'OpenWeatherMap'
        # wrf - 'weather report file'
        # owm_wrf_by_city_path imported - from paths_owm import *
        file = owm_wrf_by_city_path + '{}_{}_wrf'.format(city_name, country_or_state) + '.json'

        with open(file, 'w+') as outfile:
            json.dump(data, outfile, indent=1, ensure_ascii=False)

    # **** End of function write_wrf_content() **** #

    ###########################################################################################################
    #
    # get_owm_weather_data() will get the weather data for a city and assign to city.owm_weather_data
    #
    # example of api call to OpenWeatherMap api
    # http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={APIKEY}
    #
    # api.openweathermap.org query
    # owm_url_weather = 'http://api.openweathermap.org/data/2.5/weather?'
    # data = requests.get(owm_url_weather, params={'id': city_id, 'APPID': owm_APIKEY})
    #
    # generate_weather_report() was called with following arguments
    # city_object_list, owm_url_weather, owm_APIKEY, pb
    #
    ###########################################################################################################

    # call display_progress_bar_query_type to display query type
    display_progress_bar_query_type('weather')

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    for city in city_object_list:

        # if city.owm_weather_last_requests == '' then a requests.get has never been performed.
        # if city.perform_owm_weather_api_query() == True then it has been >= 10minutes since last requests.get
        # if either condition is True then need to do a requests.get
        if city.owm_weather_last_requests == '' or city.perform_owm_weather_api_query() == True:

            data = requests.get(owm_url_weather, params ={'id': city.owm_city_id, 'units': 'imperial', 'APPID': owm_APIKEY})
            data = data.json()

            # update the city instance attributes
            city.owm_weather_data = data
            city.owm_weather_last_requests = datetime.now()

            # write to file for debugging purposes in case the json data needs to be viewed off-line.
            write_wrf_json(data, city.city_name, city.country_or_state)

        # progress bar for query progress
        pb.query_complete += 1

        display_progress_bar(pb)
        time.sleep(.2)

        # 1. update city.owm_weather_report_run to True indicating weather report has been run for current city
        #    city this will be used by 'forecast' report to determine if current weather needs to be used during 
        #    forecast report
        city.owm_weather_report_run = True

# **** End of function get_owm_weather_data() **** #


def setup_weather_report(city_object_list):

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    # assigns updated values for attributes in city object
    for city in city_object_list:

        city.update_owm_weather_code()
        city.update_owm_temp()
        city.update_owm_wind()
        city.update_owm_visibility()
        city.update_owm_description()

# **** End of function setup_weather_report() **** #


def display_weather_report(city_object_list):

    def create_dashed_line(first, second, mid, mid_num, last):

        # assign dashed lines for the display format
        dashed_line_string = ' '

        # create first set of dashes and end with a |
        for i in range(first+1):
            if i == first:
                dashed_line_string = dashed_line_string + '|'
            else:
                dashed_line_string = dashed_line_string + '-'

        # create first set of dashes and end with a |
        for i in range(second+1):
            if i == second:
                dashed_line_string = dashed_line_string + '|'
            else:
                dashed_line_string = dashed_line_string + '-'


        # create mid sets of dashes and end each mid with a |
        # the number of mid sets = mid_num
        count = 0
        while count < mid_num:

            for i in range(mid+1):
                if i == mid:
                    dashed_line_string = dashed_line_string + '|'
                else:
                    dashed_line_string = dashed_line_string + '-'

            count += 1

        # create last set of dashes
        for i in range(last):
            dashed_line_string = dashed_line_string + '-'

        return dashed_line_string

    # **** End of function create_dashed_line() **** #

    first   = 25      # city, state or country
    second  = 30      # weather description
    mid     = 17      # temperature, wind, visibility
    mid_num = 2       # number of mid sections
    last    = 25      # weather description

    city       = 'City'
    weather    = 'Weather Condition'
    temp       = 'Temperature'
    wind       = 'Wind'
    visibility = 'Visibility'

    city       = pad_with_spaces_for_weather_report(city, first, 'title')
    weather    = pad_with_spaces_for_weather_report(weather, second, 'title')
    temp       = pad_with_spaces_for_weather_report(temp, mid, 'title')
    wind       = pad_with_spaces_for_weather_report(wind, mid, 'title')
    visibility = pad_with_spaces_for_weather_report(visibility, last, 'title')

    dashed_line_string = create_dashed_line(first, second, mid, mid_num, last)

    print(" Weather Report")
    print('\n')
    print(" {}{}{}{}{}".format(city, weather, temp, wind, visibility))
    print(dashed_line_string)

    # blank is for createing blank row
    # the blanks still need to follow the first,second,mid,last length sizes
    blank = ' '
    blank_first     = pad_with_spaces_for_weather_report(blank, first, 'blank')
    blank_second    = pad_with_spaces_for_weather_report(blank, second, 'blank')
    blank_mid       = pad_with_spaces_for_weather_report(blank, mid, 'blank')
    blank_last      = pad_with_spaces_for_weather_report(blank, last, 'blank_last')

    # create a black background for blanks
    blank_first     = (Back.BLACK + blank_first     + Style.RESET_ALL)
    blank_second    = (Back.BLACK + blank_second    + Style.RESET_ALL)
    blank_mid       = (Back.BLACK + blank_mid       + Style.RESET_ALL)
    blank_last      = (Back.BLACK + blank_last      + Style.RESET_ALL)

    # print the blank row
    print(" {}{}{}{}{}".format(blank_first, blank_second, blank_mid, blank_mid, blank_last))

    color_count = 0

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    for city in city_object_list:

        # get the dictionary data from the city.owm_weather_date attribute
        data = city.owm_weather_data

        # create city_string
        city_string   = city.city_name + ', ' + city.country_or_state

        # assign weather_descr
        weather_descr = city.owm_description

        # unicode degree symbol
        degrees = "\u00B0"

        if city.owm_temp != 'Not Available':
            # assign the city_temp string
            city_temp = int(city.owm_temp)
            city_temp = str(city_temp) + degrees + 'F'
        else:
            city_temp = city.owm_temp

        # the 'wind' may or may not be part of dictionary try and expect will prevent the crash if not available
        if city.owm_wind != 'Not Available':
            city_wind = "{0:.2f}".format(city.owm_wind) + ' mph'
        else:
            city_wind = city.owm_wind

        # the 'visibility' may or may not be part of dictionary try and expect will prevent the crash if not available
        if city.owm_visibility != 'Not Available':
            city_visibility = str(city.owm_visibility) + ' feet'
        else:
            city_visibility = city.owm_visibility

        # pad the string with spaces to prepare for colorama coloring
        city_string     = pad_with_spaces_for_weather_report(city_string, first, 'first')
        weather_descr   = pad_with_spaces_for_weather_report(weather_descr, second, 'second')
        city_temp       = pad_with_spaces_for_weather_report(city_temp, mid, 'mid')
        city_wind       = pad_with_spaces_for_weather_report(city_wind, mid, 'mid')
        city_visibility = pad_with_spaces_for_weather_report(city_visibility, last, 'last')

        if color_count == 0:
            TEXT_COLOR = Fore.YELLOW
            color_count += 1

        elif color_count == 1:
            TEXT_COLOR = Fore.CYAN
            color_count += 1

        elif color_count == 2:
            TEXT_COLOR = Fore.GREEN
            color_count += 1

        elif color_count == 3:
            TEXT_COLOR = Fore.WHITE
            color_count = 0

        # assign the colorama coloring to text
        city_string     = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + city_string     + Style.RESET_ALL)
        weather_descr   = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + weather_descr   + Style.RESET_ALL)
        city_temp       = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + city_temp       + Style.RESET_ALL)
        city_wind       = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + city_wind       + Style.RESET_ALL)
        city_visibility = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + city_visibility + Style.RESET_ALL)

        print(" {}{}{}{}{}".format(city_string, weather_descr, city_temp, city_wind, city_visibility))

    # print the blank row - all cities have been displayed
    print(" {}{}{}{}{}".format(blank_first, blank_second, blank_mid, blank_mid, blank_last))

    # print the dashed_line_string
    print(dashed_line_string)

# **** End of function display_weather_report() **** #


def pad_with_spaces_for_weather_report(var, length, position):

    # convert var to string.
    var = ' ' + str(var)
    length = length - len(var)


    if position == 'title':
        for i in range(length + 1):
            var = var + ' '

    elif position == 'blank':
        for i in range(length + 1):
            var = var + ' '

    elif position == 'blank_last':
        for i in range(length):
            var = var + ' '

    elif position == 'first' or position == 'second' or position == 'mid':
        for i in range(length + 1):
            if i == 0 or i == length or i == length - 1:
                var = var + ' '
            else:
                var = var + '.'

    elif position == 'last':
        for i in range(length):
            if i == 0 or i == length - 1:
                var = var + ' '
            else:
                var = var + '.'

    return var

# **** End of pad_with_spaces_for_weather_report() **** #


def get_owm_forecast_data(city_object_list, owm_url_forecast, owm_APIKEY, pb):

    def write_frf_json(data, city_name, country_or_state):

        # owm = 'OpenWeatherMap'
        # frf - 'forecast report file'
        # owm_frf_by_city_path imported - from paths_owm import *
        file = owm_frf_by_city_path + '{}_{}_frf'.format(city_name, country_or_state) + '.json'

        with open(file, 'w+') as outfile:
            json.dump(data, outfile, indent=1, ensure_ascii=False)

    # **** End of function write_wrf_content() **** #

    ###########################################################################################################
    #
    # get_owm_forecast_data() will get the weather data for a city and assign to city.owm_forecast_data
    #
    # example of api call to OpenWeatherMap api
    # http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
    #
    # api.openweathermap.org query
    # owm_url_forecast = 'http://api.openweathermap.org/data/2.5/forecast?'
    # data = requests.get(owm_url_weather, params={'id': city_id, 'APPID': owm_APIKEY})
    #
    # generate_forecast_report() was called with following arguments
    # city_object_list, owm_url_forecast, owm_APIKEY, pb
    #
    ###########################################################################################################

    # call display_progress_bar_query_type to display query type
    display_progress_bar_query_type('forecast')

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    for city in city_object_list:

        # if city.owm_weather_last_requests == '' then a requests.get has never been performed.
        # if city.perform_owm_weather_api_query() == True then it has been >= 10minutes since last requests.get
        # if either condition is True then need to do a requests.get
        if city.owm_forecast_last_requests == '' or city.perform_owm_forecast_api_query() == True:

            data = requests.get(owm_url_forecast, params ={'id': city.owm_city_id, 'units': 'imperial', 'APPID': owm_APIKEY})
            data = data.json()

            # wrtite the json data to the file
            write_frf_json(data, city.city_name, city.country_or_state)

            city.owm_forecast_data = data

            city.owm_forecast_last_requests = datetime.now()

        # progress bar for query progress
        pb.query_complete += 1

        display_progress_bar(pb)
        time.sleep(.2)

# **** End of function get_owm_forecast_data() **** #

def setup_forecast_report(city_object_list):

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    # assigns updated values for attributes in city object
    for city in city_object_list:

        city.find_temp_max()
        city.find_highest_priority_weather_code()
        city.set_weather_description()

# **** End of function setup_forecast_report() **** #


def display_forecast_report(city_object_list):

    def create_dashed_line_forecast_report(section, section_num):

        # assign dashed lines for the display format
        dashed_line_string = ''
        section_string = ''

        for i in range(section):
            if i == 0:
                section_string = section_string + '|'

            else:
                section_string = section_string + '-'

        count = 1
        while count <= section_num:
            dashed_line_string = dashed_line_string + section_string
            count += 1

        dashed_line_string = ' ' + dashed_line_string + '|'

        return dashed_line_string

    # **** End of function create_dashed_line_forecast_report() **** #


    def pad_day_number_title(day, section):

        length = section - len(day)

        day = ' ' + day

        for i in range(length - 2):
            day = ' ' + day

        day = day + ' '

        return day

    # **** End of function pad_day_number_title() **** #

    section      = 39      # length of each display section
    section_num  = 3       # number of display sections

    print("  Three Day Forecast")

    # titles displayed above dashed_line_string
    day1_title = "Day 1 Forecast"
    day2_title = "Day 2 Forecast"
    day3_title = "Day 3 Forecast"

    day1_title = pad_day_number_title(day1_title, section)
    day2_title = pad_day_number_title(day2_title, section)
    day3_title = pad_day_number_title(day3_title, section)

    print(" {}{}{}".format(day1_title, day2_title, day3_title))

    # create dashed line
    dashed_line_string = create_dashed_line_forecast_report(section, section_num)

    # create blank row
    #
    # each row in each section has 2 variables. blank1 and blank2 represent the 2 variables
    # for the blank row
    blank1    = ' '
    blank2    = ' '
    blank_row = pad_forecast_strings(blank1, blank2, section)
    blank_row = (Back.BLACK + blank_row + Style.RESET_ALL)

    # color_count used to change colorama colors of text
    color_count = 0

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    for city in city_object_list:

        if color_count == 0:
            TEXT_COLOR = Fore.YELLOW
            color_count += 1

        elif color_count == 1:
            TEXT_COLOR = Fore.CYAN
            color_count += 1

        elif color_count == 2:
            TEXT_COLOR = Fore.GREEN
            color_count += 1

        elif color_count == 3:
            TEXT_COLOR = Fore.WHITE
            color_count = 0

        # print dashed line
        print(dashed_line_string)

        # print blank row
        print("  {}|{}|{}".format(blank_row, blank_row, blank_row))

        # create the location variable and assign with city_name, country_or_state
        location = city.city_name + ', ' + city.country_or_state

        # get the 3 day weekday names for the forecast
        three_days = city.return_three_day_weekday_names()
        day1 = three_days[0]
        day2 = three_days[1]
        day3 = three_days[2]

        city_day1 = pad_forecast_strings(location, day1, section)
        city_day2 = pad_forecast_strings(location, day2, section)
        city_day3 = pad_forecast_strings(location, day3, section)

        city_day1 = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + city_day1 + Style.RESET_ALL)
        city_day2 = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + city_day2 + Style.RESET_ALL)
        city_day3 = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + city_day3 + Style.RESET_ALL)
        print("  {}|{}|{}".format(city_day1, city_day2, city_day3))

        # print blank row
        print("  {}|{}|{}".format(blank_row, blank_row, blank_row))

        # print blank row
        print("  {}|{}|{}".format(blank_row, blank_row, blank_row))

        # get the high temperatures for the 3 days
        # assign high_temp1,2,3 to strings
        high_temp1, high_temp2, high_temp3 = get_high_temps(three_days, city)

        # high_temp1,2,3 are type float. convert to type int
        high_temp1 = int(high_temp1)
        high_temp2 = int(high_temp2)
        high_temp3 = int(high_temp3)

        # unicode degree symbol
        degrees = "\u00B0"

        # assign high_temp1,2,3 strings
        high_temp1 = str(high_temp1) + degrees + "F"
        high_temp2 = str(high_temp2) + degrees + "F"
        high_temp3 = str(high_temp3) + degrees + "F"

        # get the weather descriptions for descr1,2,3
        descr1, descr2, descr3 = get_weather_descriptions(three_days, city)

        weather_condition1 = pad_forecast_strings(high_temp1, descr1, section)
        weather_condition2 = pad_forecast_strings(high_temp2, descr2, section)
        weather_condition3 = pad_forecast_strings(high_temp3, descr3, section)

        weather_condition1 = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + weather_condition1 + Style.RESET_ALL)
        weather_condition2 = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + weather_condition2 + Style.RESET_ALL)
        weather_condition3 = (TEXT_COLOR + Style.BRIGHT + Back.BLACK + weather_condition3 + Style.RESET_ALL)

        # print weather condition
        print("  {}|{}|{}".format(weather_condition1, weather_condition2, weather_condition3))

        # print blank row
        print("  {}|{}|{}".format(blank_row, blank_row, blank_row))

    print(dashed_line_string)

# **** End of function display_forecast_report() **** #


def pad_forecast_strings(string1, string2, section):

    string_len_sum = len(string1) + len(string2)

    string1 = ' ' + string1

    for i in range(section - string_len_sum - 3):
        string1 = string1 + ' '

    string = string1 + string2 + ' '

    return string

# **** End of function pad_forecast_strings() **** #


def get_high_temps(three_days, city):

    # high_temps to be displayed in display_forecast_report()
    # get the high_temp for each weekday in the three_day list
    if three_days[0] == 'Sunday':
        high_temp1 = city.sunday_high_temp
        high_temp2 = city.monday_high_temp
        high_temp3 = city.tuesday_high_temp

    elif three_days[0] == 'Monday':
        high_temp1 = city.monday_high_temp
        high_temp2 = city.tuesday_high_temp
        high_temp3 = city.wednesday_high_temp

    elif three_days[0] == 'Tuesday':
        high_temp1 = city.tuesday_high_temp
        high_temp2 = city.wednesday_high_temp
        high_temp3 = city.thursday_high_temp

    elif three_days[0] == 'Wednesday':
        high_temp1 = city.wednesday_high_temp
        high_temp2 = city.thursday_high_temp
        high_temp3 = city.friday_high_temp

    elif three_days[0] == 'Thursday':
        high_temp1 = city.thursday_high_temp
        high_temp2 = city.friday_high_temp
        high_temp3 = city.saturday_high_temp

    elif three_days[0] == 'Friday':
        high_temp1 = city.friday_high_temp
        high_temp2 = city.saturday_high_temp
        high_temp3 = city.sunday_high_temp

    elif three_days[0] == 'Saturday':
        high_temp1 = city.saturday_high_temp
        high_temp2 = city.sunday_high_temp
        high_temp3 = city.monday_high_temp

    return high_temp1, high_temp2, high_temp3

# **** End of function get_high_temps() **** #


def get_weather_descriptions(three_days, city):

    # descr to be displayed in display_forecast_report()
    if three_days[0] == 'Sunday':
        descr1 = city.sunday_weather_description
        descr2 = city.monday_weather_description
        descr3 = city.tuesday_weather_description

    elif three_days[0] == 'Monday':
        descr1 = city.monday_weather_description
        descr2 = city.tuesday_weather_description
        descr3 = city.wednesday_weather_description

    elif three_days[0] == 'Tuesday':
        descr1 = city.tuesday_weather_description
        descr2 = city.wednesday_weather_description
        descr3 = city.thursday_weather_description

    elif three_days[0] == 'Wednesday':
        descr1 = city.wednesday_weather_description
        descr2 = city.thursday_weather_description
        descr3 = city.friday_weather_description

    elif three_days[0] == 'Thursday':
        descr1 = city.thursday_weather_description
        descr2 = city.friday_weather_description
        descr3 = city.saturday_weather_description

    elif three_days[0] == 'Friday':
        descr1 = city.friday_weather_description
        descr2 = city.saturday_weather_description
        descr3 = city.sunday_weather_description

    elif three_days[0] == 'Saturday':
        descr1 = city.saturday_weather_description
        descr2 = city.sunday_weather_description
        descr3 = city.monday_weather_description

    return descr1, descr2, descr3

# **** End of function get_weather_descriptions() **** #


def progress_bar_scale():
    
    # create a progress bar
    blank = ' '
    print("{:>22}{}{:>24}{:>23}{:>23}{:>26}".format(blank, '0', '25%', '50%', '75%', '100%'))

# **** End of progress_bar_scale() **** #


def display_progress_bar_query_type(query_type):

    # sets up the title/query type for the query being requested
    # it is done this way so each query can over-write the previous query progress
    # display_progress_bar() will append to the print line with the actual progress indication

    if query_type == 'geocode':
        print(" Geocode Queries     ", end="", flush=True)

    elif query_type == 'city_id':
        blank_line = '\r'
        for i in range(119):
            blank_line = blank_line + ' '
        print(blank_line, end='', flush=True)
        print("\r City ID Queries     ", end="", flush=True)

    elif query_type == 'weather':
        print(" Weather Queries     ", end="")

    elif query_type == 'forecast':
        print(" Forecast Queries    ", end="")


def display_progress_bar(pb):

    # pbar is the progress bar (colored bar)
    pbar = ''

    for i in range(pb.progress_units):
        pbar = pbar + (Back.GREEN + ' ' + Style.RESET_ALL)

    if pb.query_complete == 1:
        first = ' '
        pbar = first + pbar

    # check if pb.query_complete == pb.display_width
    # if True complete remainder of progress bar to 100%. All Queries done
    if pb.query_complete == pb.list_length:
        # complete remainder of progress_bar
        # force carriage return
        pbar_remaining = pb.display_width - (pb.query_complete * pb.progress_units)

        for i in range(pbar_remaining):
            pbar = pbar + (Back.GREEN + ' ' + Style.RESET_ALL)

        # append to the printed line started by display_progress_bar_query_type()
        print(pbar, end="", flush=True)

    else:
        # append to the printed line started by display_progress_bar_query_type()
        print(pbar, end="", flush=True)

# **** End of display_progress_bar() **** #


def ctrl_c_to_quit(loop_range):

    # Press Ctrl-C to quit will flash on the screen

    for i in range(loop_range):
        try:
            print("\r Press Ctrl-C to quit", end='', flush=True),
            time.sleep(1)
            print("\r                     ", end='', flush=True)
            time.sleep(.5)
            print("\r Press Ctrl-C to quit", end='', flush=True)
            time.sleep(1)
            print("\r                     ", end='', flush=True)
            time.sleep(.5)
        except KeyboardInterrupt:
            clear_screen()
            time.sleep(.5)
            print('\n')
            thank_you_banner()
            sys.exit(0) # exit

# **** End of ctrl_c_to_quit() **** #
