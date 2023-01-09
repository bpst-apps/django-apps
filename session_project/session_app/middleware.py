from django.http import HttpResponse

class MiddleWareLifeCycle:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('before the view is executed')
        response = self.get_response(request)
        print('after the view is executed')
        return response


class ExceptionHandlingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        print(exception)
        return HttpResponse('server experiencing some issue, kindly check back in sometime ...')