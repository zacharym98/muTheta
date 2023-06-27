from django.urls import path
from . import views
from website.views import Home, About, MemberList, Join


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('members/', MemberList.as_view(), name="memberList"),
    path('join/', Join.as_view(), name="join"),
]