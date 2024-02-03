from django import forms
from django.forms import widgets


class PostForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Title', widget=widgets.TextInput(attrs={'class' : 'form-control mb-3','placeholder' : 'Title'}))
    author = forms.CharField(max_length=100, required=True, label='Author', widget=widgets.TextInput(attrs={'class': "form-control mb-3", 'placeholder' : 'Author'}))
    body = forms.CharField(max_length=3000, required=False, label='Body', widget=widgets.Textarea(attrs={'class': 'form-control mb-3', 'rows':'5', 'placeholder' : 'Body'}))