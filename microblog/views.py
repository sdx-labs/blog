from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse( '''
                        <h1>Welcome to Sean's Blog</h1>
                        <p> this website is currently under construction </p>
    ''')
