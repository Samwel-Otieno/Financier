from django import forms

from .models import *

class Create_blog(forms.ModelForm):
    class Meta:
        model=Create_blogs
        fields=['title', 'article', 'image']