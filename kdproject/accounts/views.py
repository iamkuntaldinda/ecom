from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=='POST':
        try:
            user = User()
            user.username = request.POST.get('username')
            user.set_password(request.POST.get('password'))
            user.save()
            messages.success(request,'Successfully created account')
            return redirect('login')
        except Exception as error:
            messages.error(request,error)
            return redirect('signup')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user != None:
            auth.login(request,user)
            messages.success(request,'Succesfuly loggedin')
            return redirect('/')
        else:
            messages.error(request,'Create a account to login')
            return redirect('signup')
    return render(request,'login.html')


def logout(request):
    try:
        auth.logout(request)
        messages.success(request,'Successfully Logged Out')
        return redirect('/')
    except Exception as problem:
        messages.error(request,'Failed')
        return redirect('/')