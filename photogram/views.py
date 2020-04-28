# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def numbers(request):
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))