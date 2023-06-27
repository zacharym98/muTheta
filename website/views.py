from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import MembershipRequest
from django.contrib import messages
from .models import Events, Members

# Create your views here.
class Home(View):

    form = MembershipRequest()
    events = Events.objects.all()
    context = {'form':form, 'events':events}

    def get(self, request):
        return render(request, 'home.html', self.context)
    
    def post(self, request):
        self.form = MembershipRequest(request.POST)
        if self.form.is_valid():
            self.form.save()
            messages.success(request, "Form successfully submitted!")
        return render(request, 'home.html', self.context)
    
class About(View):
    def get(self, request):
        return render(request, 'about.html')

class MemberList(View):

    members = Members.objects.all()
    context = {'members':members}

    def get(self, request):
        return render(request, 'members.html', self.context)
    
class Join(View):
    form = MembershipRequest()
    context = {'form':form}

    def get(self, request):
        return render(request, 'join.html', self.context)
    
    def post(self, request):
        self.form = MembershipRequest(request.POST)
        if self.form.is_valid():
            self.form.save()
            messages.success(request, "Form successfully submitted!")
        return render(request, 'join.html', self.context)