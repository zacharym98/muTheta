from django.forms import ModelForm
from .models import MembershipRequest


# Code added for loading form data on the Booking page
class MembershipRequest(ModelForm):
    class Meta:
        model = MembershipRequest
        fields = "__all__"