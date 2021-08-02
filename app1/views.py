
# Create your views here.
from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "date": strftime("%H:%M:%S", localtime()),
        "time": strftime("%b %d, %Y", localtime()) ,
    }
    return render(request,'index.html', context)
