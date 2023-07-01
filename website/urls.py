from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static 
from website.views import Home, About, MemberList, Join


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('members/', MemberList.as_view(), name="memberList"),
    path('join/', Join.as_view(), name="join"),
]

if settings.LOCAL_SERVE_STATIC_FILES:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.LOCAL_SERVE_MEDIA_FILES:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)