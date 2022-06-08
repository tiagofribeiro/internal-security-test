from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from bait_form.models import Usuario

def index(request):
    if request.method == "GET":
        return render(request, 'bait_form/index.html')
    else:
        username = request.POST['username']
        Usuario.objects.create(username= username)
        return HttpResponseRedirect('/success/')

def success(request):
    if request.method == "GET":
        return render(request, 'bait_form/success.html')
# Create your views here.
