from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

# import authenticate
from django.contrib.auth import authenticate, login, logout

# import User
from django.contrib.auth.models import User

# include all the tables
from . models import author, post

# forms.py er class gula import krlam
from .forms import createForm, registerUser, createAuthor


# impot messges
from django.contrib import messages


# import datetime for checking
from datetime import date

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        author_profile = author.objects.filter(name=user.id)

        if author_profile:
            authorUser = get_object_or_404(author, name=request.user.id)
            return render(request, 'index.html', {'user': authorUser, 'author_profile': author_profile})

    return render(request, 'index.html')


def getauthor(request, name):
    post_author = get_object_or_404(User, username=name)
    auth = get_object_or_404(author, name=post_author.id)
    posts = post.objects.filter(post_author=auth.id)

    context = {
        'auth': auth,
        'posts': posts 
    }

    return render(request, 'profile.html', context)



def getRegister(request):
    form = registerUser(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Registration successfully completed')
        return redirect('login')
        
    return render(request, 'register.html', {"form": form})



def getLogin(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
            user = request.POST.get('user')
            password = request.POST.get('pass')

            auth = authenticate(request, username=user, password=password) 

            if auth is not None:
                login(request, auth)
                return redirect('index')

            else:
                messages.add_message(request, messages.ERROR, 'Username and Password Mismatched.')
                return render(request, 'login.html')

    return render(request, 'login.html')


def getLogout(request):
    logout(request)
    return redirect('index')


def getcreate(request):
    if request.user.is_authenticated:
        print('id: ', request.user.id)
        u = get_object_or_404(author, name=request.user.id)

        form = createForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.post_author = u
            instance.save()
            return redirect('index')

        return render(request, 'create.html', {"form": form})
        
    else:
        return redirect('login')   


     
''' 
our previous profile

def getProfile(request): # display items
    if request.user.is_authenticated:
        posts = post.objects.filter(post_author=request.user.id)
        return render(request, 'logged_in_profile.html', {'posts':posts, 'date': date.today()})
    else:
        return redirect('login')
'''

def getProfile(request): # display items
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        author_profile = author.objects.filter(name=user.id)

        if author_profile:
            authorUser = get_object_or_404(author, name=request.user.id) 
            posts = post.objects.filter(post_author=authorUser.id)
            return render(request, 'logged_in_profile.html', {'posts':posts, 'date': date.today(), 'user': authorUser})

        else:
            form = createAuthor(request.POST or None, request.FILES or None)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.name = user 
                instance.save()
                return redirect('profile')

            return render(request, 'createauthor.html', {'form': form})


    else:
        return redirect('login')


def delete(request, list_id):
    item = post.objects.get(pk = list_id)
    item.delete()
    return redirect('profile')


def complete(request, list_id):
    item = post.objects.get(pk = list_id)
    item.completed = True
    #print('Item: ', item.Date)
    item.save()
    return redirect('profile')

 
