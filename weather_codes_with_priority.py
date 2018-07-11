######################################################################################################################
#
# owm_weather_codes dictionary: 
#   - will be used to lookup weather_codes and the 'descr' key value
#   - key 'descr' value is a summarization of 'owm_description' key value
#
# 
# 'owm_description' key and value: 
#   - is the original description from OpenWeatherMap code and is part of the dictionary
#     to preserve original weather description in case the 'descr' key value needs to be 
#     changed to a better summarization.
#
######################################################################################################################
owm_weather_priority_codes = {'codes':{
    '200':{'code': 200, 'priority': 12, 'descr': 'thunderstorm / rain','owm_description': 'thunderstorm with light rain'},
    '201':{'code': 201, 'priority': 12, 'descr': 'thunderstorm / rain','owm_description': 'thunderstorm with rain'},
    '202':{'code': 202, 'priority': 12, 'descr': 'thunderstorm / rain','owm_description': 'thunderstorm with heavy rain'},
    '210':{'code': 210, 'priority': 13, 'descr': 'thunderstorm',       'owm_description': 'light thunderstorm'},
    '211':{'code': 211, 'priority': 13, 'descr': 'thunderstorm',       'owm_description': 'thunderstorm'},
    '212':{'code': 212, 'priority': 13, 'descr': 'thunderstorm',       'owm_description': 'heavy thunderstorm'},
    '221':{'code': 221, 'priority': 13, 'descr': 'thunderstorm',       'owm_description': 'ragged thunderstorm'},
    '230':{'code': 230, 'priority': 12, 'descr': 'thunderstorm / rain','owm_description': 'thunderstorm with light drizzle'},
    '231':{'code': 231, 'priority': 12, 'descr': 'thunderstorm / rain','owm_description': 'thunderstorm with drizzle'},
    '232':{'code': 232, 'priority': 12, 'descr': 'thunderstorm / rain','owm_description': 'thunderstorm with heavy drizzle'},

    '300':{'code': 300, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'light intensity drizzle'},
    '301':{'code': 301, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'drizzle', 'owm_description': 'drizzle'},
    '302':{'code': 302, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'heavy intensity drizzle'},
    '310':{'code': 310, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'light intensity drizzle rain'},
    '311':{'code': 311, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'drizzle rain'},
    '312':{'code': 312, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'heavy intensity drizzle rain'},
    '313':{'code': 313, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'shower rain and drizzle'},
    '314':{'code': 314, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'heavy shower rain and drizzle'},
    '321':{'code': 321, 'priority': 17, 'descr': 'drizzle', 'owm_description': 'shower drizzle'},

    '500':{'code': 500, 'priority': 16, 'descr': 'rain',          'owm_description': 'light rain'},
    '501':{'code': 501, 'priority': 16, 'descr': 'rain',          'owm_description': 'moderate rain'},
    '502':{'code': 502, 'priority': 15, 'descr': 'heavy rain',    'owm_description': 'heavy intensity rain'},
    '503':{'code': 503, 'priority': 15, 'descr': 'heavy rain',    'owm_description': 'very heavy rain'},
    '504':{'code': 504, 'priority': 15, 'descr': 'heavy rain',    'owm_description': 'extreme rain'},
    '511':{'code': 511, 'priority': 14, 'descr': 'freezing rain', 'owm_description': 'freezing rain'},
    '520':{'code': 520, 'priority': 16, 'descr': 'rain',          'owm_description': 'light intensity shower rain'},
    '521':{'code': 521, 'priority': 16, 'descr': 'rain',          'owm_description': 'shower rain'},
    '522':{'code': 522, 'priority': 15, 'descr': 'heavy rain',    'owm_description': 'heavy intensity shower rain'},
    '531':{'code': 531, 'priority': 16, 'descr': 'rain',          'owm_description': 'ragged shower rain'},

    '600':{'code': 600, 'priority': 9,  'descr': 'snow',          'owm_description': 'light snow'},
    '601':{'code': 601, 'priority': 9,  'descr': 'snow',          'owm_description': 'snow'},
    '602':{'code': 602, 'priority': 8,  'descr': 'heavy snow',    'owm_description': 'heavy snow'},
    '611':{'code': 611, 'priority': 10, 'descr': 'sleet',         'owm_description': 'sleet'},
    '612':{'code': 612, 'priority': 10, 'descr': 'sleet',         'owm_description': 'shower sleet'},
    '615':{'code': 615, 'priority': 11, 'descr': 'rain and snow', 'owm_description': 'light rain and snow'},
    '616':{'code': 616, 'priority': 11, 'descr': 'rain and snow', 'owm_description': 'rain and snow'},
    '620':{'code': 620, 'priority': 9,  'descr': 'snow',          'owm_description': 'light shower snow'},
    '621':{'code': 621, 'priority': 9,  'descr': 'snow',          'owm_description': 'shower snow'},
    '622':{'code': 622, 'priority': 8,  'descr': 'heavy snow',    'owm_description': 'heavy shower snow'},

    '701':{'code': 701, 'priority': 19, 'descr': 'mist',           'owm_description': 'mist'},
    '711':{'code': 711, 'priority': 18, 'descr': 'smoke',          'owm_description': 'smoke'},
    '721':{'code': 721, 'priority': 20, 'descr': 'haze',           'owm_description': 'haze'},
    '731':{'code': 731, 'priority': 7,  'descr': 'sand',           'owm_description': 'sand, dust whirls'},
    '741':{'code': 741, 'priority': 6,  'descr': 'fog',            'owm_description': 'fog'},
    '751':{'code': 751, 'priority': 5,  'descr': 'sand',           'owm_description': 'sand'},
    '761':{'code': 761, 'priority': 4,  'descr': 'dust',           'owm_description': 'dust'},
    '762':{'code': 762, 'priority': 3,  'descr': 'volcanic ash',   'owm_description': 'volcanic ash'},
    '771':{'code': 771, 'priority': 2,  'descr': 'squalls',        'owm_description': 'squalls'},
    '781':{'code': 781, 'priority': 1,  'descr': 'tornado',        'owm_description': 'tornado'},

    '800':{'code': 800, 'priority': 24, 'descr': 'clear sky',       'owm_description': 'clear sky'},
    '801':{'code': 801, 'priority': 23, 'descr': 'few clouds',      'owm_description': 'few clouds'},
    '802':{'code': 802, 'priority': 22, 'descr': 'clouds',          'owm_description': 'scattered clouds'},
    '803':{'code': 803, 'priority': 22, 'descr': 'clouds',          'owm_description': 'broken clouds'},
    '804':{'code': 804, 'priority': 21, 'descr': 'overcast clouds', 'owm_description': 'overcast clouds'}
    } }