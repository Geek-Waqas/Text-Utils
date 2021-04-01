# created by myself
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'Home.html')
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charCounter = request.POST.get('charCounter', 'off')


    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)



    if fullcaps == "on":

        analyzed = djtext.upper()


        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}



    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")



    return render(request, 'analyze.html', params)