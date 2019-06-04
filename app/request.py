import urllib.request
import json
from .models import Quote

# getting the quotes base url

base_url = None


def configure_request(app):
    global base_url

    base_url = app.config["QUOTES_API_URL"]


def get_quotes():
    '''
    Function that gets json response to our url request
    '''

    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = process_results(get_quotes_response)

    return quotes_results


def process_results(quotes_list):
    '''
    Function that processes the quotes result and transform them to a list of Objects
    Args:
        quotes_list: A list of dictionaries that contain quote details
    Returns:
        quote_results: A list of quote objects
    '''

    quote_results = []

    for keys, value in quotes_list.items():
        if keys == 'author':
            author = value

            quote_results.append(author)

        if keys == 'quote':
            quote = value

            quote_results.append(quote)

    return quote_results