from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. This is a django boilerplate!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", home, name="home"),
]
