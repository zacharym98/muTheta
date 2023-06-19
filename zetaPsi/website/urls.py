from django.urls import path
from . import views
from website.views import Home


urlpatterns = [
    path('', Home.as_view(), name="home"),
]