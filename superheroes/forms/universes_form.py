from django import forms
from superheroes.models import Universe


class UniverseForm(forms.ModelForm):
    class Meta:
        model = Universe
        fields = [
            'name',
            'date_foundation',
            'image'
        ]
