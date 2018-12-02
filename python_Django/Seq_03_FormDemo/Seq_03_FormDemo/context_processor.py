from django.conf import settings as old_settings


def get_settings(request):
    return {"setting": old_settings}


def get_ip_address(request):
    return {"ip_address": request.META['REMOTE_ADDR']}
