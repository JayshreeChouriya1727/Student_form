from django.shortcuts import render,HttpResponse,redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == "POST":
        # check if user exist with username and password
        user = auth.authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('contact')
        else:
            return render(request,'login.html',{'error':"Invalid login Credential"})
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        # to creat a user
        if request.POST['password'] == request.POST['confirmpassword']:
            #both password match
            # check previous user exist
            try:
                user= User.objects.get(username=request.POST['username'],email= request.POST['email'])
                return render(request,'signup.html',{'error': "Username or Email has Already Been exist!!!!"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],email = request.POST['email'],
                password =request.POST['password'])
                #
                auth.login(request,user)
                return redirect(login)
        else:
            return render(request,'signup.html',{'error':"Password don't match"})    
    else:
        return render(request,'signup.html')    
    
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        courses = request.POST['courses']
        category = request.POST['category']
        desc = request.POST['desc']
        try:
            ins= Student.objects.get(phone=request.POST['phone'],email= request.POST['email'])
            return render(request,'contact.html',{'error': "number or Email has Already Been exist!!!!"})
        except Student.DoesNotExist:
            ins = Student(name=name, email=email, phone=phone, gender=gender, courses=courses, category=category, desc=desc)
            ins.save()
            return render(request,'contact.html',{'message':"Your Information Successfully Submitted..."})
        
    return render(request,'contact.html')