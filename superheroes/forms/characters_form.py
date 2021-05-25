from django import forms
from superheroes.models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'description',
            'image',
            'image2',
            'universe_id'
        ]
