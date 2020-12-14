from .models import Quote
import urllib.request,json



base_url=None

def configure_request(app):
    global base_url
    base_url=app.config['QUOTE_BASE_URL']

def get_quote():

    get_quote_url ='http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(get_quote_url) as url:

        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

    return get_quote_response

    # get_quote_url=base_url

 
