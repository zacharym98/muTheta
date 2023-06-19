from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import MembershipRequest
from django.contrib import messages

# Create your views here.
class Home(View):

    form = MembershipRequest()
    context = {'form':form}

    def get(self, request):
        return render(request, 'home.html', self.context)
    
    def post(self, request):
        self.form = MembershipRequest(request.POST)
        if self.form.is_valid():
            self.form.save()
            messages.success(request, "Form successfully submitted!")
        return render(request, 'home.html', self.context)