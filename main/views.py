import os
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Q
from django.core.context_processors import csrf

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
