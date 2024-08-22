from django import forms

from women.models import Woman


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Woman
        fields = ('title', 'content', 'is_published', 'photo', 'category', 'husband')
