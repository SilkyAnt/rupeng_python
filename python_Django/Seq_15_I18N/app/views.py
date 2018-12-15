from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


# Create your views here.
def index(request):
    i = _("Internationalization")
    sayhello = _("Welcome to Django world")
    return render(request, "Seq_01_index.html", {"i": i, "sayhello": sayhello})
