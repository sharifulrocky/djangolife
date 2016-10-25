
from django.conf.urls import url, include
from django.contrib import admin

from video.views import (home, login, registration)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^login/', login, name='login'),
    url(r'^registration/', registration, name='registration'),
]



