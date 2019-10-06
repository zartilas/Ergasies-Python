import requests


def price(symbol, comparison_symbols=['EUR', 'USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}' \
        .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data


print('BITCOIN', price('BTC', ['EUR', 'USD']))
print('LITECOIN', price('LTC', ['EUR', 'USD']))
print('ZCASH', price('ZEC', ['EUR', 'USD']))
