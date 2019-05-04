from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':68, 'placeholder':' 글을 입력하세요.'}), label='')
    img = forms.FileField(label='')
    class Meta():
        model = Post
        fields = ('img', 'title')

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' 댓글을 입력하세요.'}), label='')
    class Meta():
        model = Comment
        fields = ('comment', )