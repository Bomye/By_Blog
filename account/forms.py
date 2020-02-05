#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'YQ'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)