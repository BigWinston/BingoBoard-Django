from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from main.models import Location, Customer, Project, Staff


def index(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def board(request):
    template = loader.get_template('main/board.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def staff(request):
    template = loader.get_template('main/staff.html')
    context = {
        'staff_list': list(Staff.objects.all())
    }
    return HttpResponse(template.render(context, request))


def projects(request):
    template = loader.get_template('main/projects.html')
    context = {
        'project_list': list(Project.objects.all())
    }
    return HttpResponse(template.render(context, request))


def customers(request):
    template = loader.get_template('main/customers.html')
    context = {
        'customer_list': list(Customer.objects.all())
    }
    return HttpResponse(template.render(context, request))


def locations(request):
    template = loader.get_template('main/locations.html')
    context = {
        'location_list': list(Location.objects.all())
    }
    return HttpResponse(template.render(context, request))


def assignments(request):
    template = loader.get_template('main/assignments.html')
    context = {}
    return HttpResponse(template.render(context, request))


def backlog(request):
    template = loader.get_template('main/backlog.html')
    context = {}
    return HttpResponse(template.render(context, request))


def help(request):
    template = loader.get_template('main/help.html')
    context = {}
    return HttpResponse(template.render(context, request))

