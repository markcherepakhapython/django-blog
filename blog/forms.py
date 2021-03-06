from django import forms
from django.forms import inlineformset_factory

from .models import Post, AdditionalImage, Comment


class UserCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'post':forms.HiddenInput}


class GuestCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'post':forms.HiddenInput}


AIFormSet = inlineformset_factory(Post, AdditionalImage, fields = '__all__')
