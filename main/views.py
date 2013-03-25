# -*- coding: utf-8 -*-
import this
import os, random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader

from datetime import datetime, timedelta
from django.core.context_processors import csrf
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def channel(request):
    return render_to_response('channel.html')

def fb(request):
    print 'Facebook fb request'
    print request

def fb_auth(request):
    print 'Facebook AUTH request'
    print request

def index_db(request):
    if request.user.is_authenticated():
        c = {}
        c.update(csrf(request))
        return render_to_response('index_db.html', c)
    else:
        return render_to_response('login.html', c)
    


def register(request):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.last_name = 'Lennon'
    user.save()
    
def auth_login(request):
    print request
    username = request.POST['username']
    password = request.POST['password']
    u = User.objects.get(username__exact=username)
    if u is None:
        print 'creating user'
        user = User.objects.create_user(username, username + '@some.com', password)
    else:
        print 'user exist'
        user = u
    user.active = True
    user.save()
    user = authenticate(username=username, password=password)
    print 'user'
    print user
    if user is not None and user.is_active:
        login(request, user)
        print 'ligined'
        return render_to_response('index_db.html')
    else:
        print 'user is None'
        return render_to_response('login.html', c)
        # Return an 'invalid login' error message.