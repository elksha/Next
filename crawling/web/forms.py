from django import forms

class SearchForm(forms.Form):
    word = forms.CharField(label='Crawling Word')