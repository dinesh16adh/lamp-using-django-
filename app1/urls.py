from django.urls import path
from . import views

urlpatterns = [
    # path("home/", views.home, name="home"),
    # path("home/<str:user>/", views.home, name="home"),
    # path("welcome_page/<int:user>/", views.welcome_page, name="welcome_page"),
    # path("article/<int:year>/<int:month>", views.article, name="welcome_page"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("home/<user>/", views.home, name="home"),
]
