from json import loads
from dotenv import load_dotenv
from os import getenv
from random import randint
from requests import get, post
from sys import argv

def load_env():
    load_dotenv()
    api_key = getenv('QUOTES_ACCESS_TOKEN')
    quotes_library = getenv('QUOTES_LIBRARY')
    if quotes_library.startswith('https',0):
        quote_file = loads(get(quotes_library).text)
    else:
        quote_file = loads(open(quotes_library).read())
    return api_key, quote_file

def build_post(api_key, quote_file, choice=0):
    if choice == 0:
        rand = randint(0, len(quote_file) - 1)
    else:
        rand = choice
    quote = quote_file[rand]['quote']
    author = quote_file[rand]['author']
    toot = "'" + quote + "'\n\n - " + author + "\n\n#RandomQuote #quotes #quote #bot"
    headers = {
        "Content-Type": "application/json",
        "Bearer": api_key,
        "Authorization": "Bearer " + api_key
        }
    payload = {
        "status": toot,
        "visibility": "public"
        }
    return headers, payload

def make_post(headers, payload):
    post_endpoint = getenv('ENDPOINT')
    try:
        post(post_endpoint, json=payload, headers=headers)
    except Exception as e:
        print('An error occurred: ', e)

if __name__ == '__main__':
    if len(argv) > 0:
        choice = int(argv[1])
    else:
        choice = int(0)
    api_key, quote_file = load_env()
    headers, payload = build_post(api_key, quote_file, choice)
    make_post(headers, payload)
