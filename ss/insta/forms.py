from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':68}), label='')
    img = forms.FileField(label='')
    class Meta():
        model = Post
        fields = ('img', 'title')

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='')
    class Meta():
        model = Comment
        fields = ('comment', )