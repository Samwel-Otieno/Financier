from django import forms 

class Contact(forms.Form):
    name=forms.CharField(label='Name', max_length=30)
    email=forms.EmailField(label='Email')
    subject=forms.CharField(label='Subject', max_length=50)
    message=forms.CharField(label='Message', max_length=300, widget=forms.Textarea)
