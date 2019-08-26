from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse,HttpResponseRedirect


class MyMiddleware(MiddlewareMixin):

    def process_request(self,request):
        if request.COOKIES['userinfo']:
            return HttpResponseRedirect('/')
        return None

    def process_response(self,request,response):
        return response


class VistitLimit(MiddlewareMixin):

    visit_time={}
    def process_request(self,request):
        ip_address=request.META['']