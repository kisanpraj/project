from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def home(request):
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['password']
        subject = request.POST['subject']
        pnumber = request.POST['pnumber']

        sid = Students.objects.create(
            firstname = firstname,
            lastname = lastname,
            gender = gender,
            dob = dob,
            email = email,
            password = password,
            subject = subject,
            pnumber = pnumber,
        )

        if sid:
            context = {
                "s_msg" : "Succesfully data inserted"
            }
            return render(request,"myapp/index.html",context)
        else:
            context = {
                "s_msg": "Something went wrong"
            }
            return render(request,"myapp/index.html",context)

    return render(request, "myapp/index.html")

def dashboard(request):
    sall = Students.objects.all()
    context = {
        "sall" : sall,
    }

    return render(request,"myapp/dashboard.html",context)

def del_user(request,pk):
    sall = Students.objects.all()
    sid = Students.objects.get(id = pk)
    sid.delete()

    return redirect("dashboard")

def edit_user(request,pk):
    sid = Students.objects.get(id = pk)
    context = {
        "sid" : sid,
    }
    return render(request,"myapp/update_data.html",context)

def update_user(request):
    if request.POST:
        id = request.POST['id']
        
        sid = Students.objects.get(id = id)

        sid.firstname = request.POST['firstname']
        sid.lastname = request.POST['lastname']
        sid.gender = request.POST['gender']
        sid.email = request.POST['email']
        sid.password = request.POST['password']
        sid.dob = request.POST['dob']
        sid.subject = request.POST['subject']
        sid.pnumber = request.POST['pnumber']
        sid.save()

        return redirect("dashboard")
    
