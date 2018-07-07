###########################################################################################################
#
# assign path to OpenWeatherMap APIKEY  owm_apikey_path = 'path'
# assign path to OpenWeatherMap city.list.json  owm_city_list_json_path
# assign path to OpenWeatherMap "weather report files" (wrf)  owm_wrf_iles_by_city_path
# assign path to execution time of functions - execution_time_path
#
# owm_apikey_path ....... - OpenWeatherMap_api_key.txt has the api_key passed to api
#                 ....... - requests.get(owm_url_weather, params ={'id': city_id, 'APPID': owm_APIKEY})
#
# owm_city_list_json_path - path to the file city.list.json used to get city_id used in api query
#                         - requests.get(owm_url_weather, params ={'id': city_id, 'APPID': owm_APIKEY})
#
# owm_wrf_by_city_path .. - path to write json data returned from api call
#                         - requests.get(owm_url_weather, params ={'id': city_id, 'APPID': owm_APIKEY})
#                         - helps reduce owm_url_weather calls to every 10 minutes. If data needed before
#                           10 minute interval is up, get the data from owm_wrf_by_city_path
#
# owm_frf_by_city_path .. - path to write json data returned from api call
#                         - requests.get(owm_url_forecast, params ={'id': city_id, 'APPID': owm_APIKEY})
#                         - helps reduce owm_url_forecast calls to every 10 minutes. If data needed before
#                           10 minute interval is up, get the data from owm_wrf_by_city_path
#
# execution_time_path ... - path to write data to help measure the performance of function execution time
#                         - performing queries to geocode and owm_url_weather can experience large delays
#                           due to the api calls.
#
###########################################################################################################
owm_apikey_path         = 'C:\\Users\\Aaron\\python scripts\\APIKEYS\\OpenWeatherMap_APIKEY\\OpenWeatherMap_api_key.txt'
owm_city_list_json_path = 'C:\\Users\\Aaron\\python scripts\\Projects\\WeatherReport\\city.list.json\\city.list.json'
owm_wrf_by_city_path    = 'C:\\Users\\Aaron\\python scripts\\Projects\\WeatherReport\\owm_wrf_by_city\\'
owm_frf_by_city_path    = 'C:\\Users\\Aaron\\python scripts\\Projects\\WeatherReport\\owm_frf_by_city\\'
execution_time_path     = 'C:\\Users\\Aaron\\python scripts\\Projects\\WeatherReport\\DEBUG\\function_execution_time.txt'
