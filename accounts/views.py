from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        conformpassword = request.POST['conformpassword']
        email=request.POST['email']
        if password==conformpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("user created")
        else:
            print("password not matched")
        return redirect('/')
    else:

        return render(request,'registration.html')

class Meta:
    model = User
    fields = ('username', 'email','lastname', 'password','firstname')