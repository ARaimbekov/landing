from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя', 'class': 'form-control'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail', 'class': 'form-control', 'type':'email'}
        )
    )
    
    number = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Номер телефона', 'class': 'form-control', 'type':'char'}
        )
    )

    subject = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'placeholder': 'Тема сообщения', 'class': 'form-control', 'rows': 9}
        )
    )

    message = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение', 'class': 'form-control', 'rows': 6}
        )
    )
    