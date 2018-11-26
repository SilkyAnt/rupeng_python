from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Hello import views as hv

urlpatterns = [
    url('^index$', hv.index),
    url('^main$', hv.main),
    url('^person$', hv.person),
    url('^person2$', hv.person2),
    url('^person3$', hv.person3),
    url('^subject$', hv.subject),
    url('^r$', hv.requestDemo),
    url('^sendData$', hv.getAData),
    url('^goDataPage$', hv.goDataPage),
    url('^goFormPage$', hv.goFormPage),
    url('^login$', hv.login),
    path('admin/', admin.site.urls),
]
