from django import forms

from women.models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = ('title', 'slug', 'content', 'is_published', 'photo', 'category', 'husband')