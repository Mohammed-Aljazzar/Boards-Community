from .models import Board, Topic, Post
from django import forms


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-group','placeholder':'what is your mind?','rows':7}),help_text='The max length of the text is 4000', max_length=4000)
    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message']