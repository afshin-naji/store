from .models import Comment
from django import forms
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'user']
        labels = {
            'text': _('متن'),
            'user': _('کاربر'),
        }
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control'}),
        }

