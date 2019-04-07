from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
# from django.http import HttpResponseRedirect, HttpRe
# Create your views here.

def index(request):
	return render(request,"index.html",{})

def about(request):
	return render(request,"about.html",{})

def contact(request):
	return render(request,"contact.html",{})


def menu(request):
	return render(request,"menu.html",{})

def message(request):
	if request.method=="POST":
		print(request.POST.keys)
		name=request.POST.get("name")
		sub=request.POST.get("subject")
		message=request.POST.get("message")
		email=request.POST.get("email")
		message="Mail from:"+email+"\r"+"Name:"+name+"\r"+"Message:"+message
		send_mail(
    	sub,
    	message,
    	email,
    	['sattvikmess@gmail.com'],
    	fail_silently=False,
		)
		# index(request)
		return HttpResponse("Thanks for your suggestion "+name+", we value your suggestion.")

