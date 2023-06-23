from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        First_name = request.POST['First_name']
        Last_name = request.POST['second_name']
        Email = request.POST['E-Mail']
        Password = request.POST['Password']
        Confirm_password = request.POST['Password1']
        if Password == Confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,' this username already registered, kindly put different username')
                return redirect('register')

            elif User.objects.filter(email=Email).exists():
                 messages.info(request,' this Email already registered, kindly put different email address')
                 return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=Password, first_name=First_name,last_name=Last_name, email=Email)

            user.save();
            return redirect('login')
            messages.info(request,'registration completed')
            # print("registration completed")
        else:
            messages.info(request,'password is not matching')
            return redirect('register')
        return redirect('/')
            # print('Password not matching')

    return render(request,"register.html")