from flask import Flask

app = Flask(__name__)

@app.route('/convert/<amount>/<from_currency>/<to_currency>')

def convert_currency_api(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.9,
        'GBP': 0.7
    }
    try:
        calc = str(float(amount) / exchange_rates[from_currency] * exchange_rates[to_currency])
        result_dict = {
            'status': "Success",
            'Converted_amount': calc
        }
        return result_dict
    except KeyError:
        Error_dict ={
            "error": "Unsupported currency"
        }
        return Error_dict
    
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
