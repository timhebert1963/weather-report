from datetime import datetime
import calendar

# **** End of imports **** #

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

        # current Weather attributes
        self.owm_weather_data  = {}           # json data from OpenWeatherMap api response
        self.owm_weather_last_requests  = ''  # time when last OpenWeatherMap api requests.get occurred. do not want to do new
                                              # requests.get within 10 minutes intervals.

        # Forecast attributes
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


    def forecast_first_weekday_name(self):
        
        # find weekday_name
        # dt_txt will be a date and time string "2018-07-07 03:00:00"
        # date will be the datetime date
        # weekday_name will be the result of calendar.day_name[date.weekday()]
        dt_txt = self.owm_forecast_data['list'][0]['dt_txt']
        date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
        weekday_name = calendar.day_name[date.weekday()]

        # only 1 of the weekday names should be assigned True else: they are all False
        #
        # if all weekday names are False the current weekday name will be the first weekday name
        #   - current weekday name will be assigned True in the else: statement
        if self.sunday == True:
            pass
        elif self.monday == True:
            pass
        elif self.tuesday == True:
            pass
        elif self.wednesday == True:
            pass
        elif self.thursday == True:
            pass
        elif self.friday == True:
            pass
        elif self.saturday == True:
            pass
        else:
            if weekday_name == 'Sunday':
                self.sunday = True

            elif weekday_name == 'Monday':
                self.monday = True

            elif weekday_name == 'Tuesday':
                self.tuesday = True

            elif weekday_name == 'Wednesday':
                self.wednesday = True

            elif weekday_name == 'Thursday':
                self.thursday = True

            elif weekday_name == 'Friday':
                self.friday = True

            elif weekday_name == 'Saturday':
                self.saturday = True

    # **** End of City.forecast_first_weekday_name() **** #


    def find_temp_max(self):

        forecast_list = self.owm_forecast_data['list']

        for i in range(len(forecast_list)):
            dt_txt = self.owm_forecast_data['list'][i]['dt_txt']
            date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
            weekday_name = calendar.day_name[date.weekday()]

            high_temp = self.owm_forecast_data['list'][i]['main']['temp_max']

            # if day of week matches and high_temp is greater than day of week high_temp then update
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


    def find_highest_weather_code(self):

        # update the attributes with the highest weather code

        forecast_list = self.owm_forecast_data['list']

        for i in range(len(forecast_list)):
            dt_txt = self.owm_forecast_data['list'][i]['dt_txt']
            date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
            weekday_name = calendar.day_name[date.weekday()]

            weather_code = self.owm_forecast_data['list'][i]['weather'][0]['id']

            # if day of week matches and weather_code is greater than day of week weather_code then update
            # with weather_code

            if weekday_name == 'Sunday':
                if weather_code > self.sunday_weather_code:
                    self.sunday_weather_code = weather_code

            elif weekday_name == 'Monday':
                if weather_code > self.monday_weather_code:
                    self.monday_weather_code = weather_code

            elif weekday_name == 'Tuesday':
                if weather_code > self.tuesday_weather_code:
                    self.tuesday_weather_code = weather_code

            elif weekday_name == 'Wednesday':
                if weather_code > self.wednesday_weather_code:
                    self.wednesday_weather_code = weather_code

            elif weekday_name == 'Thursday':
                if weather_code > self.thursday_weather_code:
                    self.thursday_weather_code = weather_code

            elif weekday_name == 'Friday':
                if weather_code > self.friday_weather_code:
                    self.friday_weather_code = weather_code

            elif weekday_name == 'Saturday':
                if weather_code > self.saturday_weather_code:
                    self.saturday_weather_code = weather_code

    # **** End of City.find_highest_weather_code() **** #


    def set_weather_description(self):

        # weather codes and descriptions
        owm_codes = {'codes':{
        '200':{'code': 200, 'description': 'thunderstorm with light rain',   'icon': '11d'},
        '201':{'code': 201, 'description': 'thunderstorm with rain',         'icon': '11d'},
        '202':{'code': 202, 'description': 'thunderstorm with heavy rain',   'icon': '11d'},
        '210':{'code': 210, 'description': 'light thunderstorm',             'icon': '11d'},
        '211':{'code': 211, 'description': 'thunderstorm',                   'icon': '11d'},
        '212':{'code': 212, 'description': 'heavy thunderstorm',             'icon': '11d'},
        '221':{'code': 221, 'description': 'ragged thunderstorm',            'icon': '11d'},
        '230':{'code': 230, 'description': 'thunderstorm with light drizzle','icon': '11d'},
        '231':{'code': 231, 'description': 'thunderstorm with drizzle',      'icon': '11d'},
        '232':{'code': 232, 'description': 'thunderstorm with heavy drizzle','icon': '11d'},

        '300':{'code': 300, 'description': 'light intensity drizzle',        'icon': '09d'},
        '301':{'code': 301, 'description': 'drizzle',                        'icon': '09d'},
        '302':{'code': 302, 'description': 'heavy intensity drizzle',        'icon': '09d'},
        '310':{'code': 310, 'description': 'light intensity drizzle rain',   'icon': '09d'},
        '311':{'code': 311, 'description': 'drizzle rain',                   'icon': '09d'},
        '312':{'code': 312, 'description': 'heavy intensity drizzle rain',   'icon': '09d'},
        '313':{'code': 313, 'description': 'shower rain and drizzle',        'icon': '09d'},
        '314':{'code': 314, 'description': 'heavy shower rain and drizzle',  'icon': '09d'},
        '321':{'code': 321, 'description': 'shower drizzle',                 'icon': '09d'},

        '500':{'code': 500, 'description': 'light rain',                     'icon': '10d'},
        '501':{'code': 501, 'description': 'moderate rain',                  'icon': '10d'},
        '502':{'code': 502, 'description': 'heavy intensity rain',           'icon': '10d'},
        '503':{'code': 503, 'description': 'very heavy rain',                'icon': '10d'},
        '504':{'code': 504, 'description': 'extreme rain',                   'icon': '10d'},
        '511':{'code': 511, 'description': 'freezing rain',                  'icon': '10d'},
        '520':{'code': 520, 'description': 'light intensity shower rain',    'icon': '10d'},
        '521':{'code': 521, 'description': 'shower rain',                    'icon': '10d'},
        '522':{'code': 522, 'description': 'heavy intensity shower rain',    'icon': '10d'},
        '531':{'code': 531, 'description': 'ragged shower rain',             'icon': '10d'},

        '600':{'code': 600, 'description': 'light snow',                     'icon': '13d'},
        '601':{'code': 601, 'description': 'snow',                           'icon': '13d'},
        '602':{'code': 602, 'description': 'heavy snow',                     'icon': '13d'},
        '611':{'code': 611, 'description': 'sleet',                          'icon': '13d'},
        '612':{'code': 612, 'description': 'shower sleet',                   'icon': '13d'},
        '615':{'code': 615, 'description': 'light rain and snow',            'icon': '13d'},
        '616':{'code': 616, 'description': 'rain and snow',                  'icon': '13d'},
        '620':{'code': 620, 'description': 'light shower snow',              'icon': '13d'},
        '621':{'code': 621, 'description': 'shower snow',                    'icon': '13d'},
        '622':{'code': 622, 'description': 'heavy shower snow',              'icon': '13d'},

        '701':{'code': 701, 'description': 'mist',                           'icon': '50d'},
        '711':{'code': 711, 'description': 'smoke',                          'icon': '50d'},
        '721':{'code': 721, 'description': 'haze',                           'icon': '50d'},
        '731':{'code': 731, 'description': 'sand, dust whirls',              'icon': '50d'},
        '741':{'code': 741, 'description': 'fog',                            'icon': '50d'},
        '751':{'code': 751, 'description': 'sand',                           'icon': '50d'},
        '761':{'code': 761, 'description': 'dust',                           'icon': '50d'},
        '762':{'code': 762, 'description': 'volcanic ash',                   'icon': '50d'},
        '771':{'code': 771, 'description': 'squalls',                        'icon': '50d'},
        '781':{'code': 781, 'description': 'tornado',                        'icon': '50d'},

        '800':{'code': 800, 'description': 'clear sky',                      'icon': '01d'},
        '801':{'code': 801, 'description': 'few clouds',                     'icon': '02d'},
        '802':{'code': 802, 'description': 'scattered clouds',               'icon': '03d'},
        '803':{'code': 803, 'description': 'broken clouds',                  'icon': '04d'},
        '804':{'code': 804, 'description': 'overcast clouds',                'icon': '04d'}
        } }

        # get the desription from the owm_codes dictionary and update the self.<weekday weather_description>

        if self.sunday_weather_code != 0:
            weather_code = str(self.sunday_weather_code)
            self.sunday_weather_description = owm_codes['codes'][weather_code]['description']

        if self.monday_weather_code != 0:
            weather_code = str(self.monday_weather_code)
            self.monday_weather_description = owm_codes['codes'][weather_code]['description']

        if self.tuesday_weather_code != 0:
            weather_code = str(self.tuesday_weather_code)
            self.tuesday_weather_description = owm_codes['codes'][weather_code]['description']

        if self.wednesday_weather_code != 0:
            weather_code = str(self.wednesday_weather_code)
            self.wednesday_weather_description = owm_codes['codes'][weather_code]['description']

        if self.thursday_weather_code != 0:
            weather_code = str(self.thursday_weather_code)
            self.thursday_weather_description = owm_codes['codes'][weather_code]['description']

        if self.friday_weather_code != 0:
            weather_code = str(self.friday_weather_code)
            self.friday_weather_description = owm_codes['codes'][weather_code]['description']

        if self.saturday_weather_code != 0:
            weather_code = str(self.saturday_weather_code)
            self.saturday_weather_description = owm_codes['codes'][weather_code]['description']

    # **** End of City.set_weather_description() **** #


    def return_three_day_weekday_names(self):

        # returns a list of the first day plus the 2 days after

        if self.sunday == True:
            three_day_list = ['Sunday', 'Monday', 'Tuesday']
            return three_day_list

        elif self.monday == True:
            three_day_list = ['Monday', 'Tuesday', 'Wednesday']
            return three_day_list

        elif self.tuesday == True:
            three_day_list = ['Tuesday', 'Wednesday', 'Thursday']
            return three_day_list

        elif self.wednesday == True:
            three_day_list = ['Wednesday', 'Thursday', 'Friday']
            return three_day_list

        elif self.thursday == True:
            three_day_list = ['Thursday', 'Friday', 'Saturday']
            return three_day_list

        elif self.friday == True:
            three_day_list = ['Friday', 'Saturday', 'Sunday']
            return three_day_list

        elif self.saturday == True:
            three_day_list = ['Saturday', 'Sunday', 'Monday']
            return three_day_list

    # **** End of City.return_three_day_weekday_names() **** #

# **** End of class City() **** #
