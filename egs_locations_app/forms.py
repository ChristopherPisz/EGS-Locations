from django import forms
from .models import Playfield


class PlayfieldForm(forms.ModelForm):
    class Meta:
        model = Playfield
        fields = "__all__"
