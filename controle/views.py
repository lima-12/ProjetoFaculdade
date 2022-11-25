from django.shortcuts import render
import datetime


def home(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'controle/home.html')
