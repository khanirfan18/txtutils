from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    dj_text = request.GET.get('text','default')
    rem_punc = request.GET.get('remove_punctuations','off')
    full_caps = request.GET.get('full_caps','off')
    newline_rem = request.GET.get('newline_rem','off')
    space_rem = request.GET.get('space_rem','off')
    char_count = request.GET.get('char_count','off')
    analyzed = ""

    if rem_punc == 'on' and len(dj_text != 0):
        punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        for char in dj_text:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
     
    if full_caps == "on" and len(dj_text != 0):
        analyzed = dj_text.upper()
        params = {'purpose':'Capitalize Full','analyzed_text':analyzed}
        return render(request,"analyze.html",params)

    if newline_rem == "on" and len(dj_text != 0):
        for char in dj_text:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose':'Remove New Lines','analyzed_text':analyzed}
        return render(request,"analyze.html",params)

    if space_rem == "on" and len(dj_text != 0):
        for index,char in enumerate(dj_text):
            if dj_text[index] == " " and index != len(dj_text) - 1 and dj_text[index + 1] == " ":
                pass
            else:
                analyzed += char
        params = {'purpose':'Remove Unusual Spaces','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    if char_count == "on" and len(dj_text != 0):
        space_count = 0
        for ch in dj_text:
            if ch == " ":
                space_count+=1
            else:
                pass
        analyzed = f"there are total {len(dj_text)} characters including space and {space_count} spaces used"
        params = {'purpose':'Count characters & spaces','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else :
        return render(request,'404.html')

