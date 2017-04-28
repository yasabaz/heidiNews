# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login as userlogin, logout as userlogout
from urlparse import urlparse
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def index(request):
	return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                userlogin(request, user)
                return HttpResponseRedirect('')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})

