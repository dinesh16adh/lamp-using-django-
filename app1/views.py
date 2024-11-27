from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def home(request, user):

#     home_page_html = """
#         <!DOCTYPE html>
#         <html>
#         <body>

#         <h1>{{user}}</h1>
#         <p>my first paragraph.</p>
#         </body>
#         </html>
#     """
#     home_page_html = home_page_html.replace("{{user}}", user)

#     return HttpResponse(home_page_html)


# def welcome_page(requst, user):
#     message = "welcome to django " + str(user)
#     return HttpResponse(message)


# def article(request, year, month):
#     if month > 12:
#         return HttpResponse("this is invalid month format")
#     return HttpResponse(
#         f"<h1>this is the year {year} and month {month} from article<h1>"
#     )


def home(request, user):
    return render(request, "app1/index.html")


def contact(request):
    pass


def about(request):
    pass
