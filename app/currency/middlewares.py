import time

from currency.models import ResponseLog


class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        end = time.time()

        print(f'Response time: {end - start}') # noqa
        ResponseLog.objects.create(
            path=request.path,
            response_time=end-start,
            status_code=response.status_code,
        )
        return response

# class GclidMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if 'gclid' in request.GET:
#             print(f'Gclid in request params. Path:  {request.path}')

#         return self.get_response(request)
