from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'review', 'price', 'score')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment' : forms.Textarea(attrs={'rows':2, 'cols':60}),
        }