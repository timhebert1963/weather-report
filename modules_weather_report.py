from datetime import datetime
from timezonefinder import TimezoneFinder
from weather_codes_with_priority import *

import calendar
import pytz

# **** End of imports **** #


class ProgressBar():

    ################################################################################
    # class ProgressBar(): designed to measure the progress of queries
    #
    #
    # def __init__() will assign the list_length of the city_object_list
    #
    # list_length will be used to track the completion for all cities for each query 
    #
    ################################################################################

    def __init__(self, list_length):

        self.list_length = list_length  # queries performed against list
        self.query_complete = 0
        self.display_width  = 95   # number of characters in each row of display
        self.progress_units = int(self.display_width / self.list_length)

    # **** End of ProgressBar.__init__()

# **** End of class ProgressBar() **** #


class City():

    def __init__(self):

        self.city_name = ''          # name of city
        self.country_or_state = ''   # name of country or state - country will be long name: 'Canada' or 'England' 
                                     # ........................ - state will be abbreviated: 'TX' or 'CA'

        self.geocode_degrees = False # googlemaps geocode lat and lng. if True  self.geocode_lat and lng have int(non-0) values
                                     # ............................... if False self.geocode_lng and lng have int(0) values

        self.geocode_lat = 0         # googlemaps geocode lat degrees - returned from api as 'str' assigned as float
        self.geocode_lng = 0         # googlemaps geocode lng degrees - returned from api as 'str' assigned as float

        self.owm_city_id = 0         # OpenWeatherMap city_id

        #######################################################################################################################
        #
        # local timezone, date, time and weekday name attributes
        #
        #######################################################################################################################
        self.local_timezone     = ''    # local_timezone     format 'Europe/Vienna'
        self.local_tz_dt_txt    = ''    # local_tz_dt_txt    format '2018-07-09 16:58:00' YYYY-MM-DD HH:MM:SS
        self.local_weekday_name = ''    # local_weekday_name format 'Sunday'

        #######################################################################################################################
        #
        # current Weather attributes
        #
        #######################################################################################################################
        self.owm_weather_report_run = False   # if False weather report not run. If True weather report has been run.
        self.owm_weather_data  = {}           # json data from OpenWeatherMap api response
        self.owm_weather_last_requests  = ''  # time when last OpenWeatherMap api requests.get occurred. do not want to do new
                                              # requests.get within 10 minutes intervals.

        self.owm_weather_code = 0    # assign 0  will be updated with current weather code after query
        self.owm_description  = ''   # assign '' will be updated with current description after query
        self.owm_temp         = 0    # assign 0  will be updated with current temperature after query
        self.owm_wind         = 0    # assign 0  will be updated with current wind speed  after query
        self.owm_visibility   = 0    # assign 0  will be updated with current visibility  after query

        #######################################################################################################################
        #
        # Forecast attributes
        #
        #######################################################################################################################
        self.owm_forecast_data = {}           # json data from OpenWeatherMap api response
        self.owm_forecast_last_requests = ''  # time when last OpenWeatherMap api requests.get occurred. do not want to do new
                                              # requests.get within 10 minutes intervals.

        # assign weekday names False
        # if a date is passed in and all weekday names are False that day will be assigned True
        # if a date is passed in and one of the weekday names are True that weekday name will remain False
        # The end result is only 1 weekday name will be True and all others will remain False
        # These attributes are used to determine the 1st day of the 3 day weather forecast.
        self.sunday    = False
        self.monday    = False
        self.tuesday   = False
        self.wednesday = False
        self.thursday  = False
        self.friday    = False
        self.saturday  = False

        # the below attributes will be used for the high_temp of each day.
        # These attributes are used in the 3 day weather forecast.
        self.sunday_high_temp    = 0
        self.monday_high_temp    = 0
        self.tuesday_high_temp   = 0
        self.wednesday_high_temp = 0
        self.thursday_high_temp  = 0
        self.friday_high_temp    = 0
        self.saturday_high_temp  = 0

        # the below attributes will be used for the highest weather code of each day.
        # These attributes are used in the 3 day weather forecast.
        self.sunday_weather_code    = 0
        self.monday_weather_code    = 0
        self.tuesday_weather_code   = 0
        self.wednesday_weather_code = 0
        self.thursday_weather_code  = 0
        self.friday_weather_code    = 0
        self.saturday_weather_code  = 0

        # the below attributes will be used for the weather description of each day.
        # the weather description is derived from the weather code.
        # These attributes are used in the 3 day weather forecast.
        self.sunday_weather_description    = ''
        self.monday_weather_description    = ''
        self.tuesday_weather_description   = ''
        self.wednesday_weather_description = ''
        self.thursday_weather_description  = ''
        self.friday_weather_description    = ''
        self.saturday_weather_description  = ''

    # **** End of City.__init__() **** #


    def update_local_timezone(self):

        # set_city_tz_date_time() uses package TimezoneFinder
        # https://github.com/MrMinimal64/timezonefinder
        #
        # timezone_at()
        #   This is the default function to check which timezone a point lies within 
        #      - (similar to tzwheres tzNameAt()).
        #      - If no timezone has been found, None is being returned.
        #   PLEASE NOTE: This approach is optimized for speed and the common case to only query 
        #   points within a timezone. The last possible timezone in proximity is always returned 
        #   (without checking if the point is really included).
        #
        #   So results might be misleading for points outside of any timezone.
        #
        #   Example:
        #   longitude = 13.358
        #   latitude = 52.5061
        #   tf.timezone_at(lng=longitude, lat=latitude) # returns 'Europe/Berlin'
        #
        # certain_timezone_at()
        #   NOTE: The timezone polygons do NOT follow the shorelines any more! This causes the 
        #   computed distance from a timezone polygon to be not really meaningful/accurate.
        #
        #   Only use this when the point is not inside a polygon (simply computes and compares the 
        #   distances to the polygon boundaries!). This returns the closest timezone of all polygons 
        #   within +-1 degree lng and +-1 degree lat (or None).
        #
        #   Example:
        #   longitude = 12.773955
        #   latitude = 55.578595
        #   tf.closest_timezone_at(lng=longitude, lat=latitude) # returns 'Europe/Copenhagen'

        tf = TimezoneFinder()

        # self.local_timezone will be of string format 'Europe/London'
        self.local_timezone = tf.closest_timezone_at(lng=self.geocode_lng, lat=self.geocode_lat)
    
    # **** End of method City.update_local_timezone() **** #


    def update_local_tz_dt_txt(self):

        # self.local_tz_dt_txt will be of string format '2018-07-10 04:02:10' YYYY-MM-DD HH:MM:SS
        tz = pytz.timezone(self.local_timezone)

        # tz_now will be assigned datetime instance method datetime
        # tz_now = datetime.datetime(2018, 7, 10, 4, 2, 10, 134266, tzinfo=<DstTzInfo 'Europe/London' BST+1:00:00 DST>)
        tz_now = datetime.now(tz)

        # convert tz_now to a string and slice the date and time only
        # self.local_tz_dt_txt str format will be '2018-07-10 04:02:10'
        # this is done to be consistent with the owm forecast json 'dt_txt'
        self.local_tz_dt_txt = str(tz_now)[:19]

    # **** End of City.update_local_tz_dt_txt() **** #


    def update_local_weekday_name(self):

        # self.local_weekday_name will be of string format 'Tuesday'
        #
        # it is done this way to be consistent with the owm forecast json 'dt_txt

        date_time_string = datetime.strptime(self.local_tz_dt_txt, "%Y-%m-%d %H:%M:%S")
        self.local_weekday_name = calendar.day_name[date_time_string.weekday()]

    # **** End of City.update_local_weekday_name() **** #


    def update_owm_temp(self):

        # 'temp' key is not always avaialable in the owm_weather_data dictionary
        try:
            self.owm_temp = self.owm_weather_data['main']['temp']
        except:
            self.owm_temp = 'Not Available'

    # **** End of City.update_owm_temp() **** #


    def update_owm_wind(self):

        # 'wind' key is not always present in the owm_weather_data dictionary
        try:
            self.owm_wind = self.owm_weather_data['wind']['speed']
        except:
            self.owm_wind = 'Not Available'

    # **** End of City.update_owm_wind() **** #


    def update_owm_visibility(self):

        # 'visibility' key is not always present in the owm_weather_data dictionary
        try:
            self.owm_visibility = self.owm_weather_data['visibility']
        except:
            self.owm_visibility = 'Not Available'

    # **** End of City.update_owm_visibility() **** #


    def update_owm_weather_code(self):

        try:
            # get the weather code
            #
            # key 'id' will be used as a key for a lookup in the owm_weather_priority_codes dictionary
            # - the key will provide an index for the owm_weather_priority_codes dictionary keys and values
            # - owm_weather_priority_codes is global as it was imported in
            # - from weather_codes_with_priority import *
            self.owm_weather_code = self.owm_weather_data['weather'][0]['id']

        except:
            # self.owm_weather_data['weather'][0]['id'] lookup failed
            self.owm_weather_code = 'Not Available'

    # **** End of City.update_owm_weather_code() **** #


    def update_owm_description(self):


        # 'weather' key is not always present in the owm_weather_data dictionary

        try:
            # get the weather code id and convert to string
            #
            # str(id) will be used as a key for a lookup in the owm_weather_priority_codes dictionary
            # - the key will provide an index for the 'descr' key and value
            #
            # owm_weather_priority_codes is global as it was imported in
            # from weather_codes_with_priority import *
            code = str(self.owm_weather_code)

            self.owm_description = owm_weather_priority_codes['codes'][code]['descr']

        except:
            # self.owm_weather_data['weather'][0]['id'] lookup failed
            self.owm_description = 'Not Available'

    # **** End of City.update_owm_description() **** #


    def perform_owm_weather_api_query(self):

        # OpenWeatherMap api requests.get cannot occur within < 10 minute intervals

        # if self.owm_weather_last_requests == '' then a requests.get has never been performed. return True
        if self.owm_weather_last_requests == '':
            return True

        else:
            # if the time since owm_weather_last_requests is less than 660 seconds (11 minutes), return False
            # else: it is time to get a new requests.get
            now = datetime.now()

            if (now - self.owm_weather_last_requests).total_seconds() < 660:
                return False
            else:
                return True

    # **** End of City.perform_owm_weather_api_query() **** #


    def perform_owm_forecast_api_query(self):

        # OpenWeatherMap api requests.get cannot occur within < 10 minute intervals

        # if self.owm_weather_last_requests == '' then a requests.get has never been performed. return True
        if self.owm_forecast_last_requests == '':
            return True

        else:
            # if the time since owm_forecast_last_requests is less than 660 seconds (11 minutes), return False
            # else: it is time to get a new requests.get
            now = datetime.now()

            if (now - self.owm_forecast_last_requests).total_seconds() < 660:
                return False
            else:
                return True

    # **** End of City.perform_owm_forecast_api_query() **** #


    def find_temp_max(self):

        # determine the max temperature from the forecast query for each day of the week
        # update self.<weekday_name>_high_temp if high_temp is greater.

        forecast_list = self.owm_forecast_data['list']

        for i in range(len(forecast_list)):

            # dt_txt format will be "2018-07-09 15:00:00"
            dt_txt = self.owm_forecast_data['list'][i]['dt_txt']
            date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
            weekday_name = calendar.day_name[date.weekday()]

            high_temp = self.owm_forecast_data['list'][i]['main']['temp_max']

            # if day of week matches and high_temp is greater than <day of week>_high_temp then update
            # with high_temp

            if weekday_name == 'Sunday':

                if high_temp > self.sunday_high_temp:
                    self.sunday_high_temp = high_temp

            elif weekday_name == 'Monday':

                if high_temp > self.monday_high_temp:
                    self.monday_high_temp = high_temp

            elif weekday_name == 'Tuesday':

                if high_temp > self.tuesday_high_temp:
                    self.tuesday_high_temp = high_temp

            elif weekday_name == 'Wednesday':

                if high_temp > self.wednesday_high_temp:
                    self.wednesday_high_temp = high_temp

            elif weekday_name == 'Thursday':

                if high_temp > self.thursday_high_temp:
                    self.thursday_high_temp = high_temp

            elif weekday_name == 'Friday':

                if high_temp > self.friday_high_temp:
                    self.friday_high_temp = high_temp

            elif weekday_name == 'Saturday':

                if high_temp > self.saturday_high_temp:
                    self.saturday_high_temp = high_temp

    # **** End of City.find_temp_max() **** #


    def update_first_weather_code(self):

        # first weather code is the weather code assigned to self.owm_weather_code
        # self.<weekday name>_weather_code = self.owm_weather_code
        #
        # match on the self.local_weekday_name to find the correct self.<weekday name>_weather_code
        # to update
        if self.local_weekday_name == 'Sunday':
            self.sunday_weather_code = self.owm_weather_code

        elif self.local_weekday_name == 'Monday':
            self.monday_weather_code = self.owm_weather_code

        elif self.local_weekday_name == 'Tuesday':
            self.tuesday_weather_code = self.owm_weather_code

        elif self.local_weekday_name == 'Wednesday':
            self.wednesday_weather_code = self.owm_weather_code

        elif self.local_weekday_name == 'Thursday':
            self.thursday_weather_code = self.owm_weather_code

        elif self.local_weekday_name == 'Friday':
            self.friday_weather_code = self.owm_weather_code

        elif self.local_weekday_name == 'Saturday':
            self.saturday_weather_code = self.owm_weather_code

    # **** End of City.update_first_weather_code() **** #


    def update_first_high_temp(self):

        # first weather high temp is the weather temp assigned to self.owm_temp
        # self.<weekday name>_high_temp = self.owm_temp
        #
        # match on the self.local_weekday_name to find the correct self.<weekday name>_high_temp
        # to update
        if self.local_weekday_name == 'Sunday':
            self.sunday_high_temp = self.owm_temp

        elif self.local_weekday_name == 'Monday':
            self.monday_high_temp = self.owm_temp

        elif self.local_weekday_name == 'Tuesday':
            self.tuesday_high_temp = self.owm_temp

        elif self.local_weekday_name == 'Wednesday':
            self.wednesday_high_temp = self.owm_temp

        elif self.local_weekday_name == 'Thursday':
            self.thursday_high_temp = self.owm_temp

        elif self.local_weekday_name == 'Friday':
            self.friday_high_temp = self.owm_temp

        elif self.local_weekday_name == 'Saturday':
            self.saturday_high_temp = self.owm_temp

    # **** End of City.update_first_high_temp() **** #


    def update_first_description(self):

        # first weather description is the weather description assigned to self.owm_description
        # self.<weekday name>_weather_description = self.owm_description
        #
        # match on the self.local_weekday_name to find the correct self.<weekday name>_weather_description
        # to update
        if self.local_weekday_name == 'Sunday':
            self.sunday_weather_description = self.owm_description

        elif self.local_weekday_name == 'Monday':
            self.monday_weather_description = self.owm_description

        elif self.local_weekday_name == 'Tuesday':
            self.tuesday_weather_description = self.owm_description

        elif self.local_weekday_name == 'Wednesday':
            self.wednesday_weather_description = self.owm_description

        elif self.local_weekday_name == 'Thursday':
            self.thursday_weather_description = self.owm_description

        elif self.local_weekday_name == 'Friday':
            self.friday_weather_description = self.owm_description

        elif self.local_weekday_name == 'Saturday':
            self.saturday_weather_description = self.owm_description

    # **** End of City.update_update_first_description() **** #


    def find_highest_priority_weather_code(self):

        # update the attributes with the highest priority weather code
        # the highest priority is the lowest integer.

        forecast_list = self.owm_forecast_data['list']

        for i in range(len(forecast_list)):
            dt_txt = self.owm_forecast_data['list'][i]['dt_txt']
            date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
            weekday_name = calendar.day_name[date.weekday()]

            # f_weather_code is the forecast weather code
            # f_priority is the priority of f_weather_code
            #    - f_priority will be looked up and retrieved from the owm_weather_priority_codes dictionary
            f_weather_code = self.owm_forecast_data['list'][i]['weather'][0]['id']
            f_priority = owm_weather_priority_codes['codes'][str(weather_code)]['priority']

            # if <weekday name>_weather_code = 0:
            #    this means a valid weather code has not been assigned
            #    assign <weekday name>_weather_code to f_weather_code
            #
            # else: <if <weekday name>_weather_code != 0>
            #    get the current priority of <weekday name>_weather_code
            #
            #    if f_priority < current_priority:
            #        this means the f_priority is the highest priority
            #        assign <weekday name>_weather_code to f_weather_code

            # Sunday
            if weekday_name == 'Sunday':

                if self.sunday_weather_code == 0:
                    self.sunday_weather_code = f_weather_code

                else:
                    current_priority = owm_weather_priority_codes['codes'][str(self.sunday_weather_code)]['priority']

                    if f_priority < current_priority:
                        self.sunday_weather_code = f_weather_code

            # Monday
            elif weekday_name == 'Monday':

                if self.monday_weather_code == 0:
                    self.monday_weather_code = f_weather_code

                else:
                    current_priority = owm_weather_priority_codes['codes'][str(self.monday_weather_code)]['priority']

                    if f_priority < current_priority:
                        self.monday_weather_code = f_weather_code

            # Tuesday
            elif weekday_name == 'Tuesday':

                if self.tuesday_weather_code == 0:
                    self.tuesday_weather_code = f_weather_code

                else:
                    current_priority = owm_weather_priority_codes['codes'][str(self.tuesday_weather_code)]['priority']

                    if f_priority < current_priority:
                        self.tuesday_weather_code = f_weather_code

            # Wednesday
            elif weekday_name == 'Wednesday':

                if self.wednesday_weather_code == 0:
                    self.wednesday_weather_code = f_weather_code

                else:
                    current_priority = owm_weather_priority_codes['codes'][str(self.wednesday_weather_code)]['priority']

                    if f_priority < current_priority:
                        self.wednesday_weather_code = f_weather_code

            # Thursday
            elif weekday_name == 'Thursday':

                if self.thursday_weather_code == 0:
                    self.thursday_weather_code = f_weather_code

                else:
                    current_priority = owm_weather_priority_codes['codes'][str(self.thursday_weather_code)]['priority']

                    if f_priority < current_priority:
                        self.thursday_weather_code = f_weather_code

            # Friday
            elif weekday_name == 'Friday':

                if self.friday_weather_code == 0:
                    self.friday_weather_code = f_weather_code

                else:
                    current_priority = owm_weather_priority_codes['codes'][str(self.friday_weather_code)]['priority']

                    if f_priority < current_priority:
                        self.friday_weather_code = f_weather_code

            # Saturday
            elif weekday_name == 'Saturday':

                if self.saturday_weather_code == 0:
                    self.saturday_weather_code = f_weather_code

                else:
                    current_priority = owm_weather_priority_codes['codes'][str(self.saturday_weather_code)]['priority']

                    if f_priority < current_priority:
                        self.saturday_weather_code = f_weather_code

    # **** End of City.find_highest_priority_weather_code() **** #


    def set_weather_description(self):

        # get the desription from the owm_weather_priority_codes dictionary and update the 
        # self.<weekday_name>_weather_description
        #
        # owm_weather_priority_codes dictionary is global
        # from weather_codes_with_priority import *

        if self.sunday_weather_code != 0:
            weather_code = str(self.sunday_weather_code)
            self.sunday_weather_description = owm_weather_priority_codes['codes'][weather_code]['descr']

        if self.monday_weather_code != 0:
            weather_code = str(self.monday_weather_code)
            self.monday_weather_description = owm_weather_priority_codes['codes'][weather_code]['descr']

        if self.tuesday_weather_code != 0:
            weather_code = str(self.tuesday_weather_code)
            self.tuesday_weather_description = owm_weather_priority_codes['codes'][weather_code]['descr']

        if self.wednesday_weather_code != 0:
            weather_code = str(self.wednesday_weather_code)
            self.wednesday_weather_description = owm_weather_priority_codes['codes'][weather_code]['descr']

        if self.thursday_weather_code != 0:
            weather_code = str(self.thursday_weather_code)
            self.thursday_weather_description = owm_weather_priority_codes['codes'][weather_code]['descr']

        if self.friday_weather_code != 0:
            weather_code = str(self.friday_weather_code)
            self.friday_weather_description = owm_weather_priority_codes['codes'][weather_code]['descr']

        if self.saturday_weather_code != 0:
            weather_code = str(self.saturday_weather_code)
            self.saturday_weather_description = owm_weather_priority_codes['codes'][weather_code]['descr']

    # **** End of City.set_weather_description() **** #


    def return_three_day_weekday_names(self):

        # returns a list of the first day plus the 2 days after
        # used during the 'forecast' query

        if self.local_weekday_name == 'Sunday':
            three_day_list = ['Sunday', 'Monday', 'Tuesday']
            return three_day_list

        elif self.local_weekday_name == 'Monday':
            three_day_list = ['Monday', 'Tuesday', 'Wednesday']
            return three_day_list

        elif self.local_weekday_name == 'Tuesday':
            three_day_list = ['Tuesday', 'Wednesday', 'Thursday']
            return three_day_list

        elif self.local_weekday_name == 'Wednesday':
            three_day_list = ['Wednesday', 'Thursday', 'Friday']
            return three_day_list

        elif self.local_weekday_name == 'Thursday':
            three_day_list = ['Thursday', 'Friday', 'Saturday']
            return three_day_list

        elif self.local_weekday_name == 'Friday':
            three_day_list = ['Friday', 'Saturday', 'Sunday']
            return three_day_list

        elif self.local_weekday_name == 'Saturday':
            three_day_list = ['Saturday', 'Sunday', 'Monday']
            return three_day_list

    # **** End of City.return_three_day_weekday_names() **** #

# **** End of class City() **** #
