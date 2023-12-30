from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Travelspot

# Create your views here.
def travelspots(request):
    mytravelspots = Travelspot.objects.all().values()
    template = loader.get_template('all_travelspots.html')
    context = {
        'mytravelspots': mytravelspots,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mytravelspot = Travelspot.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mytravelspot': mytravelspot,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    mytravelspots = Travelspot.objects.all()
    template = loader.get_template('main.html')
    context = {
        'mytravelspots': mytravelspots,
    }
    return HttpResponse(template.render())

def master(request):
    mytravelspots = Travelspot.objects.all()
    template = loader.get_template('master.html')
    context = {
        'mytravelspots': mytravelspots,
    }
    return HttpResponse(template.render(context, request))