from django import forms
from .models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ["name", "email", "phone", "address1",
                  "address2", "city", "postcode", ]
