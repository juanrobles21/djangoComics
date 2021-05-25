from django import forms
from superheroes.models import Powers

class PowerForm(forms.ModelForm):
    class Meta:
        model=Powers
        fields=[
            'name',
            'image'
        ]