import requests
import json
from config import values, headers


class ConvertionException(Exception):
    pass


class ValuesConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise ConvertionException('Введите разные валюты!')

        try:
            base_ticker = values[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            quote_ticker = values[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.request('GET', f'https://api.apilayer.com/fixer/convert?to=\
{quote_ticker}&from={base_ticker}&amount={amount}', headers=headers)
        total_base = json.loads(r.content)['result']

        return total_base
