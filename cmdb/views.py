from django.shortcuts import render
from cmdb.models import Cmdb


# Create your views here.
def home(requests):
    cmdbs = Cmdb.objects
    return render(requests, 'home.html', {'cmdbs': cmdbs})
