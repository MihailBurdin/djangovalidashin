from django import forms

class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfield'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'myfield'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfield'}))

class UserFormLogin(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfield'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfield'}))