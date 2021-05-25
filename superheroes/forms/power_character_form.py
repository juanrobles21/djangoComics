from django import forms
from superheroes.models import Powers_character


class powerCharacterForm(forms.ModelForm):
    class Meta:
        model = Powers_character
        fields = [
            'powers_id',
            'character_id',
            'number'
        ]
