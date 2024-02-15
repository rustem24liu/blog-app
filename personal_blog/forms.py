from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from personal_blog.helpers.validators import at_least_3
from personal_blog.models import Tag, Author, Post


class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=200, required=True, label='Title', widget=widgets.TextInput(attrs={'class' : 'form-control mb-3','placeholder' : 'Title'}))
    # author = forms.ModelChoiceField(required=True, label='Author', queryset=Author.objects.all(), widget=widgets.Select(attrs={'class': "form-select mb-3", 'placeholder' : 'Author'}))
    # body = forms.CharField(max_length=3000, required=False, label='Body', widget=widgets.Textarea(attrs={'class': 'form-control mb-3', 'rows':'5', 'placeholder' : 'Body'}))
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label="Tags", required=False, widget=widgets.SelectMultiple(attrs={'class':'form-select'}))

    class Meta:
        model = Post
        fields = '__all__'  # ['title', 'body' ... ] smth like size

        # exclude = ['author', 'tags'] we cannot use both fields and exclude in one code, either fields or exclude
        # error_messages = '' our custom errors

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder' : 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows':'5', 'placeholder' : 'Body'}),
            'author': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Author'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('body') == cleaned_data.get('title'):
            raise ValidationError("Title is already taken")

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) < 5:
            raise ValidationError("Title is too short!")
        return title


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Author', widget=widgets.TextInput(attrs={'class' : 'form-control mb-3', 'placeholder' : 'Name'}))

class CommentForm(forms.Form):
    text = forms.CharField(max_length=1000, required=True, label='Comment', widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Comment'}))
    author = forms.CharField(max_length=200, required=True, label='Author', widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Author'}), initial="Anonymous")


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200, required=False , label='Search')