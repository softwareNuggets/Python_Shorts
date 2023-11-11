import requests
#pip install requests


def get_crypto_price(symbol):

    try:
        response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd')

        response.raise_for_status()

        crypto_price = response.json().get(symbol, {}).get('usd')

        if crypto_price is None:
            raise ValueError(f'{symbol} price not available.') 

        return crypto_price
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f'{symbol} not found. Please check the cryptocurrency symbol.')
        elif response.status_code == 429:
            print(f'Too many requests. Please wait and try again later.')
        else:
            print(f'HTTP error occurred: {http_err}')
            raise http_err
        
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
        raise req_err
    
    except Exception as error:
        print(f'An error occurred: {error}')
        raise error
    
def main():
    try:
        xrp_price = get_crypto_price('stellar')
        print(f'Current XRP Price (USD): ${xrp_price}')
    
    except Exception as error:
        print('An error occurred:', str(error))

if __name__ == "__main__":
    main()
