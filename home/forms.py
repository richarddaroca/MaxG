from django.db import models
from django import forms
from home.models import Post



class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(          # https://docs.djangoproject.com/en/1.11/ref/forms/widgets/
        attrs={                                             # adds attributes to TextInput in the form of a dictionary
            'class': 'form-control',                        # form-control is just a bootstrap class
            'placeholder': 'Write your Post here'           # placeholder is the text we see on the blank text field
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)








