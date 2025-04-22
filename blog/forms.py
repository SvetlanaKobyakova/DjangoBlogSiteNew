from django import forms
from django.contrib.auth.models import User
from .models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200, label='Заголовок')
#     text = forms.CharField(widget=forms.Textarea, label='Текст поста')
#     author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор')
#     image = forms.ImageField(required=False, label='Изображение')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')

        labels = {
            'title': 'Заголовок',
            'text': 'Текст поста',
            'image': 'Изображение',
        }


