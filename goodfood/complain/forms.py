from django import forms
from .models import Complain


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ('name', 'email', 'university_name',
                  'university_address', 'food_quality', 'further_complain'
                  )
