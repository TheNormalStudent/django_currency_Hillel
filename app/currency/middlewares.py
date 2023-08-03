import time

from currency import choices as ch
from currency.models import ResponseLog


class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        end = time.time()

        print(f'Response time: {end - start}') # noqa
        request_method = ch.REQUEST_METHODS_DICT[request.method]
        ResponseLog.objects.create(
            path=request.path,
            response_time=end-start,
            status_code=response.status_code,
            request_method=request_method
        )
        return response

# class GclidMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if 'gclid' in request.GET:
#             print(f'Gclid in request params. Path:  {request.path}')

#         return self.get_response(request)
