from django.shortcuts import render

from django.http import HttpResponse
import datetime

def current_datetime_view(request):
    now = datetime.datetime.now()
    html = "<html><body>The time now is %s.</body></html>" % now
    return HttpResponse(html)