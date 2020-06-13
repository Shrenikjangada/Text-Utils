# views.py
# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext = request.POST.get('text','default')
    purpose = ''
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.POST.get('newline','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        purpose = purpose + "Punctuations Removed "
        params = {'purpose':purpose ,'analyzed_text':analyzed}
    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        purpose = purpose + "Converted to UpperCase "
        params = {'purpose': purpose, 'analyzed_text': analyzed}
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        purpose = purpose + "Spaces Removed "
        params = {'purpose': purpose, 'analyzed_text': analyzed}
    if(newline == 'on'):
        analyzed = ''
        for char in djtext:
            if(char != '\n' and char != '\r'):
                analyzed = analyzed + char
        djtext = analyzed
        purpose = purpose + "Newline characters Removed"
        params = {'purpose': purpose, 'analyzed_text': analyzed}
    if (removepunc != "on" and fullcaps != 'on' and extraspaceremover != "on" and newline != 'on'):
        return HttpResponse("please select some operation and try again")

    return render(request, 'analyze.html', params)
