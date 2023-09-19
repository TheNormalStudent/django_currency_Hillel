TYPE_USD = 'USD'
TYPE_EUR = 'EUR'

RATE_TYPES = (
    (TYPE_USD, 'US Dollar'),
    (TYPE_EUR, "Euro"),
)

TYPE_GET = 'GET'
TYPE_POST = 'POST'
TYPE_PUT = 'PUT'
TYPE_DELETE = 'DELETE'

REQUEST_METHOD_TYPES = (
    (TYPE_GET, 'get'),
    (TYPE_POST, 'post'),
    (TYPE_PUT, 'put'),
    (TYPE_DELETE, 'delete'),
)

REQUEST_METHODS_DICT = {
    'GET': TYPE_GET,
    'POST': TYPE_POST,
    'PUT': TYPE_PUT,
    'DELETE': TYPE_DELETE
}

available_currency_types = {
    'USD': TYPE_USD,
    'EUR': TYPE_EUR,
    }
