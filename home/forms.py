from django import forms
from .models import Contact

#
# class ContactForm(forms.ModelForm):
#     class Meta :
#         model = Contact
#         fields = ['first_name','last_name','email', 'subject','message']
#         widgets ={
#             'first_name' : forms.TextInput(attrs={'class':'input','placeholder':'firstname'}),
#             'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'lastname'}),
#             'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
#             'subject': forms.TextInput(attrs={'class': 'input', 'placeholder': 'subject','height':'50px;'}),
#             'message': forms.Textarea(attrs={'class': 'input', 'placeholder': 'write your message'}),
#         }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    # catid = forms.IntegerField()
