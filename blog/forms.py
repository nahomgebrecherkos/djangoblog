from django import forms
from .models import postModel, Comment

class PostModleFrom(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = postModel
        fields = ('title', 'content')

class PostUpdateFrom(forms.ModelForm):
    class Meta:
        model = postModel
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Type your comment here"}))
    class Meta:
        model = Comment
        fields = ('content',)