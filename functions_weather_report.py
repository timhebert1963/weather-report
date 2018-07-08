from modules_weather_report import *
from paths_owm import *
from datetime import datetime
from colorama import Fore, Back, Style, init
init(autoreset = True)

import time
import requests
import json
import codecs
import os
import googlemaps

# **** End of imports **** #

def execution_TIME(message, *args):

    ############################################################################################
    #
    #   *args will have 2 or 3 arguments
    #     - 2 args, 'start', start_time
    #     - 3 args, 'finished', start_time, finished_time
    #
    #   execution_TIME() will write to file in execution_time_path. The content of the file will 
    #   record the time a function started and finished and the number of seconds it took to
    #   execute the function.
    #
    ############################################################################################
    start = args[1]

    if args[0] == 'start':

        time = str(start.hour) + ':' + str(start.minute) + '.' + str(start.second) + '.' + str(start.microsecond)

        message = message + "START TIME    = {}\n".format(time)

    elif args[0] == 'finished':

        finished = args[2]
        time = str(finished.hour) + ':' + str(finished.minute) + '.' + str(finished.second) + '.' + str(finished.microsecond)
        difference = (finished - start).total_seconds()

        message = message + "FINISHED TIME = {}: TOTAL RUN TIME = {} seconds\n\n".format(time, difference)

    # execution_time_path is imported - from paths_owm import *
    f = open(execution_time_path, 'a')
    f.write(message)
    f.close()

# **** End of function execution_TIME() **** #


def welcome_to_weather_report_banner():

    #first = 8
    #mid   = 15 * 5
    #last  = 30
    #center = first + mid + last
    line_len = 118

    # assign string to display in display_banner()
    first_string  = "Welcome to Weather Report"
    second_string = "Weather Report: displays Weather Condition, Temperature, Wind and Visibility"
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
    print('\n')

# **** End of welcome_to_stock_quotes_banner() **** #


def welcome_to_forecast_report_banner():

    #first = 8
    #mid   = 15 * 5
    #last  = 30
    #center = first + mid + last
    line_len = 118

    # assign string to display in display_banner()
    first_string  = "Welcome to Forecast Report"
    second_string = "Weather Forecast: displays 5 day Forecast for Weather Condition, Temperature, Wind and Visibility"
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
    print('\n')

# **** End of welcome_to_stock_quotes_banner() **** #


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
        valid_string = True

        while valid_string == True:
            country_or_state = input(" Enter the long name for country or abbreviated state for the city of {}:  ".format(city)).upper()

            # check for len(city) == 0
            # user pressed 'Enter' and did not input a string
            if len(country_or_state) == 0:
                print(" A country or state name was not entered. Please Try Again.")

            else:
                valid_string = False
                return country_or_state

    # **** End of function enter_more_city_names() **** #


    def enter_more_city_names():

        is_answer_valid = False

        while not is_answer_valid:
            answer = input(" Do you want to add another city to the Weather Report? 'y' or 'n'  ")

            if answer.lower() == 'y' or answer.lower() == 'yes' or answer.lower() == 'n' or answer.lower() == 'no':
                return answer
            else:
                print(" You did not enter 'y' or 'n'. Please Try Again.")

    # **** End of function enter_more_city_names() **** #

    enter_city_names = True

    while enter_city_names == True:

        print('\n')

        city = input(" Enter the city name for Weather Report:  ").title()

        # check for len(city) == 0
        # user pressed 'Enter' and did not input a string
        if len(city) == 0:
        	print(" A city name was not entered. Please Try Again.")

        else:

            country_or_state = enter_country_or_state()

            # check to ensure user entered a valid city, country_or_state
            # does_city_exist() will return True or False
            result = does_city_exist(city, country_or_state)

            if not result:
                print(" A valid city name was not entered. Please Try Again, and enter a valid city")

            else:
                city_names_list.append((city, country_or_state))
                answer = enter_more_city_names()

                if answer.lower() != 'y' and answer.lower()!= 'yes':

                    return city_names_list

                else:
                    pass     # more city, country_or_state names will be added to the city_names_list

# **** End of function get_city_names_for_weather_report() **** #


def does_city_exist(city, country_or_state):

    # Log start time
    start_time = datetime.now()
    time_message = "TIME: does_city_exist() "
    execution_TIME(time_message, 'start', start_time)

    ###########################################################################################################
    #
    # does_city_exist() will determine if the city, country_or_state are valid
    # - need to loop through the ['address_components']['long_name'] because not all cities have the same
    #   number of 'long_name' keys and the key values are not in the same order.
    #
    ###########################################################################################################

    # api_key for googlemaps geocode api
    geocode_api_key = os.environ['APIKEY']

    # start googlemaps Client
    gm = googlemaps.Client(key=geocode_api_key)

    for i in range(len(gm.geocode((city, country_or_state))[0]['address_components'])):

        try:
            # get the long_name from geocode
            name = gm.geocode((city, country_or_state))[0]['address_components'][i]['long_name']

            # compare the city name and name from geocode
            # if true then return True
            if city.lower() == name.lower():

                # Log finished time
                finished_time = datetime.now()
                time_message = "TIME: does_city_exist() "
                execution_TIME(time_message, 'finished', start_time, finished_time)

                return True

        except Exception as message:
            # catch exception messages and pass
            pass

    # Log finished time
    finished_time = datetime.now()
    time_message = "TIME: does_city_exist() "
    execution_TIME(time_message, 'finished', start_time, finished_time)

    # if no match return False
    return False

# **** End of function does_city_exist() **** #


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

    # Log start time
    start_time = datetime.now()
    time_message = "TIME: get_geocode_degrees() "
    execution_TIME(time_message, 'start', start_time)

    # api_key for googlemaps geocode api
    geocode_api_key = os.environ['APIKEY']
    
    # start googlemaps Client
    gm = googlemaps.Client(key=geocode_api_key)

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

    # Log finished time
    finished_time = datetime.now()
    time_message = "TIME: get_geocode_degrees() "
    execution_TIME(time_message, 'finished', start_time, finished_time)

# **** End of function get_geocode_degrees() **** #


def get_city_id(city_object_list, pb):

    ###########################################################################################################
    #
    # Need to pass City ID to OpenWeatherMap api for accuracy
    # - match the geocode lat and lon with the OpenWeatherMap lat and lon
    # - when the match occurs then extract the city_id out of the OpenWeatherMap json dictionary
    #
    ###########################################################################################################

    # Log start time
    start_time = datetime.now()
    time_message = "TIME: get_city_id() "
    execution_TIME(time_message, 'start', start_time)

    # open and read the file city.list.json which has the city_id
    # owm_city_list_json_path is imported - from paths_owm import *
    open_file = open(owm_city_list_json_path, 'r', encoding='utf-8')
    read_file = json.loads(open_file.read())
    open_file.close()

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    for city in city_object_list:

        # if city.owm_city_id == 0 then update city.owm_city_id = owm_city_id
        # else: city.owm_city_id already has valid city_id assigned -> do nothing 
        if city.owm_city_id == 0:

            # loop through the read_file and assign owm_name
            # if owm_name == city:
            #     check to see if int(geocode_lat) == int(owm_lat) and int(geocode_lng) == int(owm_lon)
            #     if this is true then assign city_id to   
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
                        break

        # progress bar for query progress
        pb.query_complete += 1

        display_progress_bar(pb)
        time.sleep(.1)

    # Log finished time
    finished_time = datetime.now()
    time_message = "TIME: get_city_id() "
    execution_TIME(time_message, 'finished', start_time, finished_time)

# **** End of function get_city_id() **** #


def get_owm_weather_data(city_object_list, owm_url_weather, owm_APIKEY, pb):

    def write_wrf_json(data, city_name, country_or_state):

        # owm = 'OpenWeatherMap'
        # wrf - 'weather report file'
        # owm_wrf_by_city_path imported - from paths_owm import *
        file = owm_wrf_by_city_path + '{}_{}'.format(city_name, country_or_state) + '.json'

        with open(file, 'w+') as outfile:
            json.dump(data, outfile, indent=1, ensure_ascii=False)

    # **** End of function write_wrf_content() **** #

    ###########################################################################################################
    #
    # example of api call to OpenWeatherMap api
    # http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={APIKEY}
    #
    # api.openweathermap.org querye
    # owm_url_weather = 'http://api.openweathermap.org/data/2.5/weather?'
    # data = requests.get(owm_url_weather, params={'id': city_id, 'APPID': owm_APIKEY})
    #
    # generate_weather_report() was called with following arguments
    # city_object_list, owm_url_weather, owm_APIKEY, pb
    #
    ###########################################################################################################

    # Log start time
    start_time = datetime.now()
    time_message = "TIME: get_owm_weather_data() "
    execution_TIME(time_message, 'start', start_time)

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

    # Log finished time
    finished_time = datetime.now()
    time_message = "TIME: get_owm_weather_data() "
    execution_TIME(time_message, 'finished', start_time, finished_time)

# **** End of function get_owm_weather_data() **** #


def setup_weather_report(city_object_list):

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    # assigns updated values for attributes in city object
    for city in city_object_list:

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
    weather    = 'Weather'
    temp       = 'Temperature'
    wind       = 'Wind'
    visibility = 'Visibility'

    city       = pad_with_spaces_for_weather_report(city, first, 'title')
    weather    = pad_with_spaces_for_weather_report(weather, second, 'title')
    temp       = pad_with_spaces_for_weather_report(temp, mid, 'title')
    wind       = pad_with_spaces_for_weather_report(wind, mid, 'title')
    visibility = pad_with_spaces_for_weather_report(visibility, last, 'title')

    dashed_line_string = create_dashed_line(first, second, mid, mid_num, last)

    print('\n')
    print('\n')
    print(" Weather Report")
    print('\n')
    print(" {}{}{}{}{}".format(city, weather, temp, wind, visibility))
    print(dashed_line_string)

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

        # assign the city_temp string
        city_temp     = int(city.owm_temp)
        city_temp     = str(city_temp) + degrees + 'F'

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

    print(dashed_line_string)
    print('\n')

# **** End of function display_weather_report() **** #


def pad_with_spaces_for_weather_report(var, length, position):

    # convert var to string.
    var = str(var)
    length = length - len(var)


    if position == 'title':
        for i in range(length + 1):
            var = var + ' '

    elif position == 'first' or position == 'second' or position == 'mid':
        for i in range(length + 1):
            if i == 0 or i == length:
                var = var + ' '
            else:
                var = var + '.'

    elif position == 'last':
        for i in range(length):
            if i == 0:
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
        file = owm_frf_by_city_path + '{}_{}'.format(city_name, country_or_state) + '.json'

        with open(file, 'w+') as outfile:
            json.dump(data, outfile, indent=1, ensure_ascii=False)

    # **** End of function write_wrf_content() **** #

    ###########################################################################################################
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

    # Log start time
    start_time = datetime.now()
    time_message = "TIME: get_owm_weather_data() "
    execution_TIME(time_message, 'start', start_time)

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    for city in city_object_list:

        # if city.owm_weather_last_requests == '' then a requests.get has never been performed.
        # if city.perform_owm_weather_api_query() == True then it has been >= 10minutes since last requests.get
        # if either condition is True then need to do a requests.get
        if city.owm_forecast_last_requests == '' or city.perform_owm_forecast_api_query() == True:

            data = requests.get(owm_url_forecast, params ={'id': city.owm_city_id, 'units': 'imperial', 'APPID': owm_APIKEY})
            data = data.json()

            # REMOVE after completely debugged
            write_frf_json(data, city.city_name, city.country_or_state)

            city.owm_forecast_data = data

            city.owm_forecast_last_requests = datetime.now()

        # progress bar for query progress
        pb.query_complete += 1

        display_progress_bar(pb)
        time.sleep(.2)

    # Log finished time
    finished_time = datetime.now()
    time_message = "TIME: get_owm_weather_data() "
    execution_TIME(time_message, 'finished', start_time, finished_time)

# **** End of function get_owm_forecast_data() **** #

def setup_forecast_report(city_object_list):

    # loop through each item in city_object_list 
    # city_object_list = [city1_object, city2_object, etc..]
    # assigns updated values for attributes in city object
    for city in city_object_list:

        city.forecast_first_weekday_name()
        city.find_temp_max()
        city.find_highest_weather_code()
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

    section      = 39      # length of each display section
    section_num  = 3       # number of display sections

    # create dashed line
    dashed_line_string = create_dashed_line_forecast_report(section, section_num)

    # create blank row
    blank1    = ' '
    blank2    = ' '
    blank_row = pad_forecast_strings(blank1, blank2, section)
    blank_row = (Back.BLACK + blank_row + Style.RESET_ALL)

    print("  Three Day Forecast")

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


def progress_bar_scale(query_type):
    
    # create a progress bar
    blank = ' '
    print("{:>22}{}{:>24}{:>23}{:>23}{:>26}".format(blank, '0', '25%', '50%', '75%', '100%'))

    if query_type == 'geocode':
        print(" Geocode Queries     ", end="")

    elif query_type == 'city_id':
        print(" City ID Queries     ", end="")

    elif query_type == 'weather':
        print(" Weather Queries     ", end="")

# **** End of progress_bar_scale() **** #


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

        print(pbar)

    else:
        print(pbar, end="")

# **** End of display_progress_bar() **** #
