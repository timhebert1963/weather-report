from functions_weather_report import *
from Tim_common import *
import time

# **** End of imports **** #


def run_weather_report(owm_url_weather, owm_APIKEY, city_names_list):

    ###########################################################################################################
    #
    # args passed in to run_weather_report()
    # - owm_url_weather arg: api to weather reports per city_id
    # - owm_APIKEY arg: api key for OpenWeatherMap pass in as a parameter to owm_url_weather
    # - city_names_list arg: list of tuples (city_name, country_or_state) used to retrieve coordinates (lat/lon),
    #   'city_id', etc. city_names_list is like the master list of city names and all data structures will need
    #   to be in sync with the items in the list.
    #
    ###########################################################################################################

    ###########################################################################################################
    # 
    # 1. PRINT HEADING OF PROGRESS BAR
    #    - a progress bar will be displayed to notify user of the stock query 
    #      progress
    #    - print the heading of the progress bar
    #    - create an instance of the class ProgressBar()
    #
    #    class ProgressBar() attributes are updated and evaluated during the 
    #    stock queries to determine progress of the queries.
    #
    ###########################################################################################################
    clear_screen()
    time.sleep(.5)
    print('\n')
    welcome_to_weather_report_banner()

    progress_bar_scale('geocode')
    pb = ProgressBar(len(city_names_list))

    ###########################################################################################################
    #
    # 2. call get_geocode_degrees()
    #    - get the city, country_or_state lat and lng (latitude and longitude) for each city in city_names_list
    #    - googlemaps geocode lat and lng will be used to lookup the city_id when calling get_city_id()
    #    - assign class_object.lat and class_object.lng with geocode lat and lng respectively
    #
    ###########################################################################################################
    get_geocode_degrees(city_names_list, pb)
    time.sleep(.5)

    ###########################################################################################################
    #
    # 3. ASSIGN pb.query_complete = 0
    #    - need to assign to 0 now that all queries are complete
    #    - this will allow Progress Bar to start at 0% for the next "new" set of stock queries. 
    #
    ###########################################################################################################
    pb.query_complete = 0

    ###########################################################################################################
    # 
    # 4. PRINT HEADING OF PROGRESS BAR
    #    - a progress bar will be displayed to notify user of the stock query progress
    #    - print the heading of the progress bar
    #    - create an instance of the class ProgressBar()
    #
    #    class ProgressBar() attributes are updated and evaluated during the 
    #    stock queries to determine progress of the queries.
    #
    ###########################################################################################################
    clear_screen()
    time.sleep(.5)
    print('\n')
    welcome_to_weather_report_banner()

    progress_bar_scale('city_id')

    ###########################################################################################################
    #
    # 5. call get_city_id()
    #    - get the city_id for each city in city_names_list
    #    - city_id will be used when getting the weather statics for that city
    #    - assign city_object.owm_city_id = city_id
    #
    ###########################################################################################################
    get_city_id(city_names_list, pb)
    time.sleep(.5)

    ###########################################################################################################
    #
    # 6. ASSIGN pb.query_complete = 0
    #    - need to assign to 0 now that all queries are complete
    #    - this will allow Progress Bar to start at 0% for the next "new" set of
    #      stock queries. 
    #
    ###########################################################################################################
    pb.query_complete = 0

    ###########################################################################################################
    # 
    # 7. PRINT HEADING OF PROGRESS BAR
    #    - a progress bar will be displayed to notify user of the stock query progress
    #    - print the heading of the progress bar
    #    - create an instance of the class ProgressBar()
    #
    #    class ProgressBar() attributes are updated and evaluated during the 
    #    stock queries to determine progress of the queries.
    #
    ###########################################################################################################
    clear_screen()
    time.sleep(.5)
    print('\n')
    welcome_to_weather_report_banner()

    progress_bar_scale('weather')

    ###########################################################################################################
    #
    # 8. call get_owm_weather_data()
    #    - the weather statistics for each city, country_or_state will be collected
    #
    ###########################################################################################################
    get_owm_weather_data(city_names_list, owm_url_weather, owm_APIKEY, pb)
    time.sleep(2)

    ###########################################################################################################
    #
    # 9. ASSIGN pb.query_complete = 0
    #    - need to assign to 0 now that all queries are complete
    #    - this will allow Progress Bar to start at 0% for the next "new" set of
    #      stock queries. 
    #
    ###########################################################################################################
    pb.query_complete = 0

    ###########################################################################################################
    #
    # 10. call display_weather_report()
    #     - the weather statistics for each city, country_or_state will be collected
    #
    ###########################################################################################################
    clear_screen()
    time.sleep(.5)
    print('\n')
    welcome_to_weather_report_banner()

    display_weather_report(city_names_list)
    print('\n')
    print(" Press Ctrl-C to quit")
    time.sleep(5)

# **** End of function run_weather_report() **** #


class ProgressBar():

    ################################################################################
    # class ProgressBar(): designed to measure the progress of stock quote queries
    #
    # There will be 2 types of queries performed when getting stock quotes. 
    #    1. current_day  quote query 
    #    2. previous_day quote query
    #
    # def __init__() will assign the length of the symbol_list * 2 (1 for each type 
    # of query)
    #
    # length will be used to track the completion of each query (1 for each item in
    # symbol_list)
    ################################################################################

    def __init__(self, list_length):

        self.list_length = list_length  # queries performed against list
        self.query_complete = 0
        self.display_width  = 95   # number of characters in each row of display
        self.progress_units = int(self.display_width / self.list_length)

    # **** End of ProgressBar.__init__()

# **** End of class ProgressBar() **** #