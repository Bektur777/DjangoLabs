from django import forms

from .models import ReviewBook


class ReviewBookForm(forms.ModelForm):
    class Meta:
        model = ReviewBook
        fields = '__all__'
        widgets = {
            'text_review': forms.TextInput(attrs={'placeholder': 'Введите комментарий'}),
        }
