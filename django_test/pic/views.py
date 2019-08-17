
from django.http import HttpResponse
from django.shortcuts import render
from pic.models import Picture,Topic,User


def up_file(request):

    if request.method == 'GET':
        return render(request, 'up_file.html')
    else:
        #正常的会u为request.u    拿出用户的entry对象
        u=User.objects.create(username='dahaigui')
        content=request.POST.get('content','')
        t=Topic.objects.create(content=content,username=u)
        imgs=request.FILES.getlist('myfile')
        for img in imgs:
            p=Picture.objects.create(img=img,topic=t,user=u)
        return HttpResponse('ok')