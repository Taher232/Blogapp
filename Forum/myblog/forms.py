from django import forms
from . models import Post, Category, Comment, Video

choices = Category.objects.all().values_list('name', 'name')
# choices = []

choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'snippet', 'author',
                  'category', 'body', 'header_image', 'video_file')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your snippet here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),

            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content here'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment here'}),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']
