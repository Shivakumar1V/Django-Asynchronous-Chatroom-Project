from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from chat_app.models import Chatroom, Chat

# Create your views here.

def index(request):
    return render(request, 'index.html')


def chatRoom(request, room_name):
    chatroom = Chatroom.objects.filter(name=room_name).first()
    chats = []
    if chatroom:
        chats = Chat.objects.filter(room=chatroom)
    else:
        chatroom = Chatroom(name=room_name)
        chatroom.save()
    
    return render(request, 'chat_room.html', {'room_name': room_name, 'chats': chats})


def loginHandler(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('loginpass')
        user_check = authenticate(username=username, password=password)
        if user_check is not None:
            login(request, user_check)
            messages.success(request, "Successfully Loggedin")
            return redirect("/")
        else:
            messages.warning(request, "Incorrect Username or Password")
            return redirect("/")
        

def signupHandler(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('signuppass1')
        pass2 = request.POST.get('signuppass2')
        user_exist = User.objects.filter(username=username)
        if user_exist:
            messages.warning(request, "Username is already exist")
            return redirect("/")
        else:
            if pass1 == pass2:
                signup_user = User.objects.create_user(username=username, password=pass1)
                signup_user.save()
                user_log = authenticate(username=username, password=pass1)
                login(request, user_log)
                messages.success(request, "Your account has been created successfully")
                return redirect("/")
            else:
                messages.warning(request, "Password do not match")
                return redirect("/")


def logoutHandler(request):
    logout(request)
    return redirect("/")
