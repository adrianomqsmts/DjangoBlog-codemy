from django import forms
from .models import Post, Category, Comment

# choices = (('coding','coding'),('movies', 'movies'),('others'. 'other'),)
choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    """Form definition for Post."""

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ('title', 'title_tag', 'category',
                  'author', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title for post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': "", 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    """Form definition for Post."""

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ('title', 'title_tag',  'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title tp post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title tp post'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
