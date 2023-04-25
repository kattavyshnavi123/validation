from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse

def student(request):
    SFO=Studentform()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=Studentform(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))

        else:
            return HttpResponse('data is not valid')
    return render(request,'student.html',d)    

