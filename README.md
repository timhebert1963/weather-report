# weather-report

Python version 3.6.4
Only tested on Windows 8.1

Requirements:

    OpenWeatherMap
    - uses OpenWeatherMap api, so you will need to get a api key from OpenWeatherMap
    - https://openweathermap.org/price get the free api key
    - http://bulk.openweathermap.org/sample/  and download and unzip city.list.json.gz

    Googlemaps Geocode api
    - you will need a googlemaps geocode api key and set proper environment variables
    - youtube videos as a reference
      - https://www.youtube.com/watch?v=1MVDIFShE5Q&t=57s
      - https://www.youtube.com/watch?v=sI8py6soTWs

    Colorama needs to be pip installed (pip install colorama)

    path_owm.py file - you need to provide proper paths in the path_owm.py file

        owm_apikey_path         = 'path\OpenWeatherMap_api_key.txt'  <- .txt file with api key
        - enter 3 lines below in your .txt file. It will just work if you use the 3 lines below
        - enter your api key number in replacement of <your api key number>

            OpenWeatherMap  https://openweathermap.org/
            Current Weather api_key = <your api key number>
            <your api key number>

        owm_city_list_json_path = 'path\city.list.json'  <- city.list.json.gz unzipped location

        owm_wrf_by_city_path = 'path'  <- script will write json files to this location for each city
        - file sizes are not big and they will not grow over time.

        execution_time_path = 'path\function_execution_time.txt'  <- google geocode queries and openweathermap 
                                                                     queries performance tracked here.
