mock_history_data = {
        "coord": [
            50.0,
            50.0
        ],
        "list": [
            {
            "main": {
                "aqi": 2
            },
            "components": {
                "co": 270.367,
                "no": 5.867,
                "no2": 43.184,
                "o3": 4.783,
                "so2": 14.544,
                "pm2_5": 13.448,
                "pm10": 15.524,
                "nh3": 0.289
            },
            "dt": 1606482000
            },
            {
            "main": {
                "aqi": 2
            },
            "components": {
                "co": 280.38,
                "no": 8.605,
                "no2": 42.155,
                "o3": 2.459,
                "so2": 14.901,
                "pm2_5": 15.103,
                "pm10": 17.249,
                "nh3": 0.162
            },
            "dt": 1606478400
            }]
    }

mock_forecast_data = {
        "coord": [
            50.0,
            50.0
        ],
        "list": [
            {
            "main": {
                "aqi": 2
            },
            "components": {
                "co": 270.367,
                "no": 5.867,
                "no2": 43.184,
                "o3": 4.783,
                "so2": 14.544,
                "pm2_5": 13.448,
                "pm10": 15.524,
                "nh3": 0.289
            },
            "dt": 1606482000
            },
            {
            "main": {
                "aqi": 2
            },
            "components": {
                "co": 280.38,
                "no": 8.605,
                "no2": 42.155,
                "o3": 2.459,
                "so2": 14.901,
                "pm2_5": 15.103,
                "pm10": 17.249,
                "nh3": 0.162
            },
            "dt": 1606478400
            }]
    }

mock_api_invalid_key_error = {
   'cod': 401, 
   'message': 'Invalid API key. Please see http://openweathermap.org/faq#error401 for more info.' 
   }

mock_params = {
   'lat': 49.28,
   'lon': 123.12,
   'start': 1606488670,
   'end': 1606747870,
   'appid': 'mock_api_key'
}

mock_incorrect_params = {
   'lat': 'latitude_val',
   'lon': 'longitude_val',
   'start': 1234.567,
   'end': 3.14159,
   'appid': 'invalid_api_key'
}