from django.forms import ModelForm
from .models import MembershipRequest


# Code added for loading form data on the Booking page
class MembershipRequest(ModelForm):
    class Meta:
        model = MembershipRequest
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Last Name'})
        self.fields['graduation_year'].widget.attrs.update({'placeholder':'Graduation Year'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})