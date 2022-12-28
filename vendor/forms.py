from dataclasses import field
import django


from django import forms
from django import forms

from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = [
            "vendor_name",
            "vendor_license"
        ]
