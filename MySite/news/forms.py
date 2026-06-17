from django import forms
from .models import Category, News
from django.core.exceptions import ValidationError

def validate_no_digit_start(value):
    if value and value[0].isdigit():
        raise ValidationError('Заголовок не может начинаться с цифры')

class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=255, 
        label='Заголовок', 
        validators=[validate_no_digit_start],
        widget=forms.TextInput(attrs={'class': 'form-control'})  
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), 
        label='Текст', 
        required=False
    )
    is_published = forms.BooleanField(
        initial=True, 
        label='Опубликовано',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})  
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        label='Категория', 
        empty_label='-----',
        widget=forms.Select(attrs={'class': 'form-control'})  
    )

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=100,
        label='Автор',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    text = forms.CharField(
        label='Текст комментария',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

class NewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
            'category': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Текст',
            'is_published': 'Опубликовано',
            'category': 'Категория'
        }