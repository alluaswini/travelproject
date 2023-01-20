from django.shortcuts import render
# Create your views here.
def fun(request):
    return render(request,'index.html')

def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})

