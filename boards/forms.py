from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Type your post here.'}
        ),
        max_length=4000,
        help_text='The max length of this text is 4000 characters.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']
