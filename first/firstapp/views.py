from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    # my_dict = {'insert_me' : "Index page"}
    # return render(request,'firstapp/index.html',context = my_dict)
    return render(request,'firstapp/index.html',context = date_dict)

def help(request):
    my_dict = {'insert_me' : "Help page"}
    return render(request,'firstapp/help.html',context = my_dict)


