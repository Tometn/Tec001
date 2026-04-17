from flask import Flask, request

app = Flask(__name__)

@app.route('/get_weather/<city_name>')
def get_weather_endpoint(city_name):
    city_info = {
          'HCM': {
                "Temp": 25,
                "Condition": "Sunny",
                "Forcast": [30, 29, 31]
          },
           'HN': {
                "Temp": 34,
                "Condition": "Rainy",
                "Forcast": [32, 34, 31]
           }
    }
    
    return city_info[city_name]

if __name__ == '__main__':
        app.run(use_reloader=True, host='127.0.0.1', port=5000)