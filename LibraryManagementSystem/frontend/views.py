from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse , HttpResponseRedirect
import re
from User_Profile.models import Profile
from Library.models import *
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import uuid
import time
# Create your views here.

def login_or_signup(request):
    return render(request,'frontend/login_or_signup.html')

def signup(request):
    username = request.POST['username']
    password = make_password(request.POST['password'])
    email = request.POST['email']
    phone = request.POST['phone']
    role = int(request.POST['role'])
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    #profile_id = uuid.uuid1().hex
    if(username=='' or  password=='' or email=='' or phone== '' or first_name=='' or last_name=='' or (role>4 and role<1)):
        data = {
            'success': False,
            'message': 'Something went wrong! Try again!',
        }
    else:
        try:
            user = User(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            profile = Profile.objects.get(user=user)
            profile.phone=phone
            profile.role=role
            profile.save()
            data = { 
                'success': True,
                'message': 'Account is created successfully!',
            }
        except:
            data = {
            'success': False,
            'message': 'Username already exists! Try again!',
            }
    return JsonResponse(data)

def signin(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #request.session['fav_color'] = 'blue'
                return HttpResponseRedirect('/index')
    #return render_to_response('login.html', context_instance=RequestContext(request))
    messages.error(request, 'Authentication Failure!')
    return render(request,'frontend/authentication_failure.html')

@login_required
def index(request):
    book_lists = Book.objects.all()
    book_list = []
    user_requested_book_list = BookTransaction.objects.filter(created_by=request.user)
    for book in book_lists:
        fg = 0
        #try:
        book_transaction_list = BookTransaction.objects.filter(book=book)
        for book_transaction in book_transaction_list:
            if((book_transaction.request_status != "Requested" and book_transaction.request_status != "Returned") or (book_transaction.created_by.username==request.user.username)):
                fg = 1
        
        # except:
        #     pass
        if(fg == 0):
            book_list.append(book)
    data = {
        'book_list':book_list,
        'user_requested_book_list':user_requested_book_list,
        }
    return render(request,'frontend/index.html',data)

def logout_view(request):
    logout(request)
    return render(request,'frontend/logout.html')

def requestBook(request):
    #time.sleep(3)
    try:
        book_id = request.POST['book_id']
        book = Book.objects.get(book_id=book_id)
        transaction_id = uuid.uuid1().hex
        bookTransaction = BookTransaction(transaction_id=transaction_id,book=book,request_status="Requested",payment_status="N/A",created_by=request.user)
        bookTransaction.save()
        data = {
            'success': True,
            'message': 'Request sent successfully!',
        }
    except:
        data = {
        'success': False,
        'message': 'Something went wrong!',
        }
    return JsonResponse(data)