from screenshare_server.views.rest_dispatch import RESTDispatch
from django.http import HttpResponse
from screenshare_server.upload_processing import handle_uploaded_file
from datetime import timedelta
import json
import re

CURRENT_LIST_MAX_DAYS = 3


class UploadView(RESTDispatch):
    """
    Handles uploading a screenshot
    """
    def POST(self, request, current=False):
        source = request.POST['source']
        file = None
        for key in request.FILES:
            file = request.FILES[key]
        handle_uploaded_file(file, source)
        return HttpResponse('Success')