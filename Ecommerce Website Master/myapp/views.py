from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        try:
            if request.POST["name"] == "" or request.POST["email"] == "" or request.POST["subject"] == "" or request.POST["message"] == "":
                context = {
                "msg_d" : "All fields are mandatory..."
            }
                return render(request, "contact.html", context=context)    
            else:
                contact = Contact.objects.create(
                    name = request.POST["name"],
                    email = request.POST["email"],
                    subject = request.POST["subject"],
                    message = request.POST["message"],
                ) 
                contact.save()
                subject = 'Message Sent status : SUCCESSFUL'
                message = f'Hi {contact.name}, Thank you for contacting us.\n\nOur team will get back to you within 24 hours.\n\nBest Regards....'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [contact.email, ]
                send_mail( subject, message, email_from, recipient_list )

                subject = f'Contact Request sent by {contact.name} | {contact.subject}'
                message = f"MESSAGE : \n{contact.message}"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [settings.EMAIL_HOST_USER, ]
                send_mail( subject, message, email_from, recipient_list )

                context = {
                    "msg_s" : "Contact request sent successfully..."
                }
                return render(request, "contact.html", context=context)
        except Exception as e:
            print(f"\n\n\n{e}\n\n\n")
            context = {
                "msg_d" : "Something went wrong..."
            }
            return render(request, "contact.html", context=context)
    else:
        return render(request, "contact.html")


def signup(request):
    if request.method == "POST":
        try:
            if request.POST["fname"] == "" or request.POST["lname"] == "" or request.POST["email"] == "" or request.POST["phone"] == "" or request.POST["address"] == "" or request.POST["password"] == "" or request.POST["re_password"] == "": 
                context = {
                    "msg_d" : "*All fields are mandatory"
                }
                return render(request, "signup.html", context=context)    
            elif request.POST["password"] == request.POST["re_password"]:
                user = Buyer.objects.create(
                    fname = request.POST["fname"], 
                    lname = request.POST["lname"], 
                    email = request.POST["email"], 
                    phone = request.POST["phone"], 
                    address = request.POST["address"], 
                    password = request.POST["password"], 
                )
                user.save()
                subject = 'Account status : CREATED'
                message = f'Hi {user.name}, Jodava Badal Aabhar'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )

                context = {
                    "msg_s" : "Account created succes"
                }
                return render(request, "signup.html", context=context)
            else:
                context = {
                    "msg_d" : "Password and Repeat Password does not match..."
                }
                return render(request, "signup.html", context=context)    
        except Exception as e:
            print(f"\n\n\n{e}\n\n\n")
            context = {
                "msg_d" : "Something went wrong..."
            }
            return render(request, "signup.html", context=context)
    else:
        return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")