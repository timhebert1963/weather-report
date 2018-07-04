from datetime import datetime

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
        self.owm_weather_data = {}   # json data from OpenWeatherMap api response

        self.owm_last_requests = ''  # time when last OpenWeatherMap api requests.get occurred. do not want to do new
                                     # requests.get within 10 minutes intervals.

    # **** End of City.__init__() **** #


    def perform_owm_api_query(self):

        # OpenWeatherMap api requests.get cannot occur within < 10 minute intervals

        # if self.owm_last_requests == '' then a requests.get has never been performed. return True
        if self.owm_last_requests == '':
            return True

        else:
            # if the time since owm_last_requests is less than 660 seconds (11 minutes), return False
            # else: it is time to get a new requests.get
            now = datetime.now()

            if (now - self.owm_last_requests).total_seconds() < 660:
                return False
            else:
                return True

    # **** End of City.how_many_minutes() **** #    

# **** End of class City() **** #