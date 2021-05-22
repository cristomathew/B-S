from django.shortcuts import render, redirect, get_object_or_404
from Core.models import User
from listings.models import Listing
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password

from inquiry.models import inquiry
from listings.forms import UpdateForm
import random
import string

def randomString(stringlength=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringlength))

code = randomString()

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        user = User

        context ={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'phone': phone,
            'password': password,
        }

        if password == password2:
            if user.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                if user.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already used')
                    return redirect('register')
                else:
                    if user.objects.filter(phone=phone).exists():
                        messages.error(request, 'Phone no  is already used')
                        return redirect('register')
                    else:
                        send_mail(
                            'Account Creation Confirmation',
                            'Hi '+ first_name + ' You Confirmation code is: ' +code,
                            'cristomathew7@gmail.com',
                            [email],
                            fail_silently=False
                        )
                        request.method = 'GET'
                        return render(request, 'accounts/confirmregister.html', context)
        else:
            messages.error(request,'passwords donot match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def confirmregister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmcode = request.POST['confirmcode']
        user = User
        context ={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'phone': phone,
            'password': password,
        }
        if code == confirmcode:
            user = user.objects.create_user(username=username, email=email, password=password,  phone=phone, first_name=first_name, last_name=last_name)
            user.save()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Confirmation Code')
            return render(request, 'accounts/confirmregister.html', context)
    else:
        return redirect('register')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

@login_required
def userlogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "you are now logged out")
        return redirect('index')

@login_required
def dashboard(request):
    mylistings = Listing.objects.order_by('-list_date').filter(owner=request.user)
    context = {
        'listings': mylistings
    }
    return render(request, 'accounts/dashboard.html', context)
@login_required
def favourite_listing(request):
    favourites = request.user.favourites
    favourites = favourites.split(',')[1:]
    print(favourites)
    listings = []
    for i in favourites:
        listings.append(get_object_or_404(Listing,pk=int(i)))
    context = {
        'listings': listings
    }
    return render(request, 'accounts/favourites.html', context)
@login_required
def myinquiries(request):
    myinquiry = inquiry.objects.all().filter(user_id=request.user.id)
    context = {
        'myinquiries': myinquiry
    }
    return render(request, 'accounts/dashboard_myinquiries.html', context)
@login_required
def inquiry1(request):
    myinquiry = inquiry.objects.all().filter(owner_id=request.user.id)
    context = {
        'inquiries': myinquiry
    }
    return render(request, 'accounts/dashboard_inquiries.html', context)

@login_required
def send_reply(request):
    if request.method =="POST":
        email = request.POST['email']
        message = request.POST['message']
        lisiting = request.POST['listing']
        send_mail(
            'Reply from ' + lisiting + ' owner',
            message,
            'cristomathew7@gmail.com',
            [email],
            fail_silently=False
        )
        messages.success(request, 'Your reply has been sent successfully')
        return redirect('inquiry1')
    else:
        return redirect('dashboard')


@login_required
def change_password(request):
    if request.method=='POST':
        user = request.user
        currentpassword = request.POST['currentpassword']
        if not check_password(currentpassword,user.password):
            messages.error(request,'Incorrect Current Password')
            return redirect('dashboard')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user.set_password(password1)
            user.save()
            messages.success(request,'You have been logged out')
            messages.success(request,'You have successfully changed the password')
            messages.success(request,'Use your new password to login')
        else:
            messages.error(request,'Passwords do not match')
        return redirect('dashboard')
    
    else:
        return render(request,'accounts/change_password.html')
