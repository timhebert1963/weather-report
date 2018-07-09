from functions_weather_report import *
from Tim_common import *
import time

# **** End of imports **** #

###############################################################################################################
#
# Two function and one class exists in this file
# - get_city_coordinates()
# - def run_report()
# - class ProgressBar()
#
###############################################################################################################


def get_city_coordinates(city_object_list):

    ###########################################################################################################
    # 
    # 1. PRINT WELCOME BANNER
    #
    ###########################################################################################################
    clear_screen()
    time.sleep(.5)
    print('\n')

    welcome_banner()

    ###########################################################################################################
    # 
    # 2. PRINT HEADING OF PROGRESS BAR
    #    - a progress bar will be displayed to notify the user of the query progress
    #    - print the heading of the progress bar
    #    - create an instance of the class ProgressBar()
    #
    #    pb instance attributes are updated and evaluated during the 
    #    query to determine progress of the geocode query.
    #
    ###########################################################################################################
    progress_bar_scale()
    pb = ProgressBar(len(city_object_list))

    ###########################################################################################################
    #
    # 3. call get_geocode_degrees()
    #    - get the city, country_or_state lat and lng (latitude and longitude) for each city in city_object_list
    #    - googlemaps geocode lat and lng will be used to lookup the city_id when calling get_city_id()
    #    - will assign city.lat and city.lng with geocode lat and lng respectively
    #
    ###########################################################################################################
    get_geocode_degrees(city_object_list, pb)
    time.sleep(1)

    ###########################################################################################################
    #
    # 4. ASSIGN pb.query_complete = 0
    #    - need to assign to 0 now query is complete
    #    - this will allow Progress Bar to start at 0% for the next "new" query. 
    #
    ###########################################################################################################
    pb.query_complete = 0

    ###########################################################################################################
    #
    # 5. call get_city_id()
    #    - get the city_id for each city in city_object_list
    #    - city_id will be used when getting the weather or forecast statistics for that city
    #    - assign city.owm_city_id = city_id
    #
    ###########################################################################################################
    get_city_id(city_object_list, pb)
    time.sleep(1)

    ###########################################################################################################
    #
    # 6. ASSIGN pb.query_complete = 0
    #    - need to assign to 0 now that query is complete
    #    - this will allow Progress Bar to start at 0% for the next "new" query.
    #
    ###########################################################################################################
    pb.query_complete = 0

# **** End of function get_city_coordinates() **** #


def run_report(owm_url_weather, owm_url_forecast, owm_APIKEY, city_object_list, report):

    ###########################################################################################################
    #
    # args passed in to run_report()
    # - owm_url_weather arg: api to weather reports per city_id
    # - owm_APIKEY arg: api key for OpenWeatherMap pass in as a parameter to owm_url_weather
    # - city_object_list arg: list of city objects for each city being tracked in weather report
    # - report: determines if this will be a 'weather' report or a 'forecast' report
    #
    ###########################################################################################################

    ###########################################################################################################
    # 
    # 1. PRINT WEATHER OR FORECAST REPORT BANNER
    #
    ###########################################################################################################
    clear_screen()
    time.sleep(.5)
    print('\n')

    if report == 'weather':
        weather_report_banner()
    elif report == 'forecast':
        forecast_report_banner()

    ###########################################################################################################
    # 
    # 2. PRINT HEADING OF PROGRESS BAR
    #    - a progress bar will be displayed to notify the user of the query progress
    #    - print the heading of the progress bar
    #    - create an instance of the class ProgressBar()
    #
    #    pb instance attributes are updated and evaluated during the 
    #    query to determine progress of the geocode query.
    #
    ###########################################################################################################
    progress_bar_scale()
    pb = ProgressBar(len(city_object_list))

    ###########################################################################################################
    #
    # 3. CHECK VALUE OF REPORT
    #         if report   == 'weather':  call get_owm_weather_data()
    #         elif report == 'forecast': call get_owm_forecast_data()
    #
    #     - get_owm_weather_data() and get_owm_forecast_data() will get json data and populate each city 
    #       instance attributes.
    #
    ###########################################################################################################
    if report == 'weather':
        get_owm_weather_data(city_object_list, owm_url_weather, owm_APIKEY, pb)
    elif report == 'forecast':
        get_owm_forecast_data(city_object_list, owm_url_forecast, owm_APIKEY, pb)

    time.sleep(2)

    ###########################################################################################################
    #
    # 4. ASSIGN pb.query_complete = 0
    #    - need to assign to 0 now that query is complete
    #    - this will allow Progress Bar to start at 0% for the next "new" query.
    #
    ###########################################################################################################
    pb.query_complete = 0

    ###########################################################################################################
    #
    # 5. assign values to each city instance attributes for the weather or forecast report
    #
    ###########################################################################################################
    if report == 'weather':
        setup_weather_report(city_object_list)
    elif report == 'forecast':
        setup_forecast_report(city_object_list)

    ###########################################################################################################
    # 
    # 6. PRINT WEATHER OR FORECAST REPORT BANNER
    #
    ###########################################################################################################
    clear_screen()
    time.sleep(.5)
    print('\n')

    if report == 'weather':
        weather_report_banner()
    elif report == 'forecast':
        forecast_report_banner()

    ###########################################################################################################
    #
    # 7. call display_weather_report() or display_forecast_report()
    #     - the statistics for each city, country_or_state report will be displayed to user.
    #
    ###########################################################################################################
    if report == 'weather':
        display_weather_report(city_object_list)
    elif report == 'forecast':
        display_forecast_report(city_object_list)

    print('\n')
    print(" Press Ctrl-C to quit")
    time.sleep(20)

# **** End of function run_report() **** #


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