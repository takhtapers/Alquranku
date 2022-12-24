from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path ,include

from . views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404,handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('content.urls')),
    path('', home, name='home'),
    path('alquran', alquran, name='alquran'),
    path('doa/', doa, name='doa'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),

    path('login', login, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register, name='register'),

]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, decument_root=settings.MEDIA_ROOT)