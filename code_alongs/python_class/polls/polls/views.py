from django.http import HttpResponse
import random

def index(request):
    return HttpResponse("You are in the polls index.")

def hello_world(request):
    return HttpResponse("Hello World")


def random_number(request,max_rand):
    random_number = random.randrange(0,int(max_rand))

    msg = "Random number between 0 and %s : % d" % (max_rand, random_number)
    return HttpResponse(msg)