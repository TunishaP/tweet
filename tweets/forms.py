from dataclasses import fields
from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'

class PictureForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'