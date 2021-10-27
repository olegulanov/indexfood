from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', mainpage, name='Home'),
    path('about', about, name='About'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'), 
    path('register', RegisterUser.as_view(), name='register'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)