from django import forms

from women.models import Women


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = ('title', 'content', 'is_published', 'photo', 'category', 'husband')
