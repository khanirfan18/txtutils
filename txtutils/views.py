from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    dj_text = request.GET.get('text','default')
    checkbox_info = request.GET.get('remove_punctuations','off')
    print(checkbox_info,"=",dj_text)
    analyzed = dj_text
    params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
    return render(request,"analyze.html",params)
