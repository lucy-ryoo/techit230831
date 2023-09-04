from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import Registration


# Create your views here.

def hello_world(request):
    if request.method == "POST":
        email = request.POST.get('email')

        reg = Registration()
        reg.email = email
        reg.save()

        reg_all = Registration.objects.all()



        return render(request, "accountapp/hello_world.html",
                      context={"temp": email,
                               "reg_all": reg_all})

    temp = "techit"
    return render(request, "accountapp/hello_world.html",
                  context={"temp": temp})

