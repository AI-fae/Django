from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import ResourcesForm

# Create your views here


def home(request):
    return render(request, 'resource/homepage.html')

def contact(request):
    return HttpResponse("we would like to hear from you. contact us")

def about(request):
    return render(request, 'resource/aboutpage.html')

def content(request):

    materials = Resources.objects.all()
    visitors = Visitor.objects.all()
    total_visitors = visitors.count()
    total_resources = materials.count()
    web_info = {"resources":materials, 'total_visitors': total_visitors, 'total_resources': total_resources}
    return render(request, 'resource/content.html', web_info)

def services(request):
    return HttpResponse("we offer quality services at very affordable prices. reach us")

def visitor(request, pk=1):
    user = Visitor.objects.get(id=pk)
    visitors = VisitLog.objects.filter(id=pk)
    resources = Resources.objects.filter(id=pk)
    visit_info = {"visitors": visitors, "resources": resources, "user": user}
    return render(request, 'resource/visitors.html', visit_info)

def createForm(request):

    form = ResourcesForm()
    if request.method == 'POST':
       # print('printing POST:', request.POST)
        form = ResourcesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')

    context = {'form':form}
    return render(request, 'resource/form.html', context)
