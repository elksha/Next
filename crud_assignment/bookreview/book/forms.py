from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'review', 'price', 'score', 'picture')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment' : forms.Textarea(attrs={'rows':2, 'cols':60}),
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'password': forms.PasswordInput()
            }