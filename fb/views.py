# Create your views here.
import hashlib
import urllib
import time
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.conf import settings
import facebook
import datetime



def fb_auth(request):
    v_code = request.GET.get('code')
    APP_ID = settings.FACEBOOK_APP_ID
    FB_P=settings.FB_PERM
    if 'fbs_' + APP_ID in request.COOKIES and not v_code:
        user = authenticate(cookies=request.COOKIES)
        if user:
            login(request, user)
            next_redirect = request.GET.get('next','')
            if(next_redirect):
                return HttpResponseRedirect(next_redirect)
            elif(settings.FB_AUTH_REDIRECT):
                return HttpResponseRedirect(settings.FB_AUTH_REDIRECT)
            else:
                return HttpResponseRedirect("/")
        else:
            pass
            #resp.delete_cookie('fbs_' + APP_ID,path="/")
            #return resp
    elif(v_code):
        user = authenticate(verification_code=v_code)
        if user:
            login(request, user)
        access_token = user.facebook.select_related()[0].access_token
        '''
        if request.META.has_key('HTTP_REFERER'):
            url = request.META['HTTP_REFERER']
            resp=HttpResponseRedirect(urllib2.unquote(url))
        else:
            resp=HttpResponseRedirect("http://"+settings.SESSION_COOKIE_DOMAIN)
        '''
        next_redirect = request.GET.get('next','')
        if(next_redirect):
            return HttpResponseRedirect(next_redirect)
        elif(settings.FB_AUTH_REDIRECT):
            resp =  HttpResponseRedirect(settings.FB_AUTH_REDIRECT)
        else:
            resp =  HttpResponseRedirect("/")
        if(FB_P.count('offline_access')):
            resp=set_cookie(resp, "fbs_"+APP_ID, str(user.username),access_token=access_token,expires=datetime.datetime.utcnow() + datetime.timedelta(days=30))
        else:
            resp=set_cookie(resp, "fbs_"+APP_ID, str(user.username),access_token=access_token,expires=datetime.datetime.utcnow() + datetime.timedelta(hours=2))
        return resp

    ur = 'http://' + request.get_host() + request.path
    perm=",".join(FB_P)
    args = dict(client_id=APP_ID, redirect_uri=ur, scope=perm)
    resp = HttpResponseRedirect("https://graph.facebook.com/oauth/authorize?" + urllib.urlencode(args))
    resp.delete_cookie('fbs_' + APP_ID)
    return resp


def set_cookie(resp, name, value, access_token=None, domain=None, path="/", expires=None):

    """Generates and signs a cookie for the give name/value"""
    if(not expires):
        expires = datetime.datetime.utcnow() + datetime.timedelta(hours=2)

    args = {}
    args['expires'] = expires.now().strftime('%s')
    args['uid'] = value
    if(access_token):   
        args['access_token'] = access_token
        graph = facebook.GraphAPI(access_token)
        graph=graph.get_object('me')
        fname = graph['first_name']
        args['fname']=fname

    signature = cookie_signature(args)
    args['sig'] = signature
    #resp.set_cookie(name,urllib.urlencode(args),path="/",domain=settings.SESSION_COOKIE_DOMAIN,expires=str(int(time.time())+21600000))
    resp.set_cookie(name,urllib.urlencode(args), expires=expires, path='/', domain=settings.SESSION_COOKIE_DOMAIN, secure=None)
    return resp

def cookie_signature(parts):
    """Generates a cookie signature.

    We use the Facebook app secret since it is different for every app (so
    people using this example don't accidentally all use the same secret).
    """
    payload = ''
    for part in sorted(parts.keys()):
        payload += part+"="+str(parts[part])
    payload += settings.FACEBOOK_SECRET_KEY
    return hashlib.md5(payload).hexdigest() 
