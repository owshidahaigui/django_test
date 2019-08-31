from django.shortcuts import render

from django.http import HttpResponse
from .tasks import task_test

# Create your views here.


def users(request):
    c = request.COOKIES.get('username')
    resp = HttpResponse('set cookie is ok')
    print(request.session.get('username', ''))
    request.session['username'] = 'dahaigui'
    resp.set_cookie('username', 'dahaigui', 60)
    return resp


def test_csrf(request):
    # csrf攻击网站

    return render(request, 'test_csrf.html')


def test_csrf_server(request):
    print(111111111111111111)
    print(request.GET.keys())
    print('over')
    return HttpResponse('dfsda')
