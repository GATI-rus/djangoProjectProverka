from django import forms

class UserComment(forms.Form):
    name = forms.CharField(max_length=10, label='Имя')
    no_robot = forms.BooleanField(error_messages={'required': 'поставьте галочку'})
    comment = forms.CharField(widget=forms.Textarea, label='Коментарий',
                              min_length=10,
                              error_messages={'min_lenght': 'минимум 10 слов'})
    email = forms.EmailField(required=False)