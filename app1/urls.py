from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("welcome_page/<str:user>/", views.welcome_page, name="welcome_page"),
    path("welcome_page/<int:user>/", views.welcome_page, name="welcome_page"),
    path("article/<int:year>/<int:month>", views.article, name="welcome_page"),
]
