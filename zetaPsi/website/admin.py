from django.contrib import admin
from .models import MembershipRequest, Events

# Register your models here.
admin.site.register(MembershipRequest)
admin.site.register(Events)