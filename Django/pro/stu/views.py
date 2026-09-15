from django.shortcuts import render
from stu.models import *

def home_view(req):
    data = stu_m.objects.all()
    context={
        "student": data,

    }
    return render(req, "home.html", context)