from django.shortcuts import render,HttpResponse
from .models import Student
# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        courses = request.POST['courses']
        category = request.POST['category']
        desc = request.POST['desc']
        ins = Student(name=name, email=email, phone=phone, gender=gender, courses=courses, category=category, desc=desc)
        ins.save()
        print("the data has been written to dp")
    return render(request,'contact.html')