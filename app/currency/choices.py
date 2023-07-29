TYPE_USD = 'USD'
TYPE_EUR = 'EUR'

RATE_TYPES = (
    (TYPE_USD, 'US Dollar'),
    (TYPE_EUR, "Euro"),
)

TYPE_GET = 'GET'
TYPE_POST = 'POST'

REQUEST_METHOD_TYPES = (
    (TYPE_GET, 'get'), 
    (TYPE_POST, 'post'),
)

REQUEST_METHODS_DICT = {
    'GET': TYPE_GET,
    'POST': TYPE_POST
}

available_currency_types = {
    'USD': TYPE_USD,
    'EUR': TYPE_EUR,
    }
