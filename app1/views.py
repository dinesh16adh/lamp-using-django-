from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("hello world")


def welcome_page(requst, user):
    message = "welcome to django " + str(user)
    return HttpResponse(message)


def article(request, year, month):
    if month > 12:
        return HttpResponse("this is invalid month format")
    return HttpResponse(
        f"<h1>this is the year {year} and month {month} from article<h1>"
    )
