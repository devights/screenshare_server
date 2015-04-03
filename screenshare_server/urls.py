from django.conf.urls import include, url
from django.contrib import admin
from screenshare_server.views.upload_view import UploadView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    url(r'upload/', csrf_exempt(UploadView().run)),
]
