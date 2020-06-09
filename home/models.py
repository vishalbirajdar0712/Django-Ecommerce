from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from crispy_forms.helper import FormHelper

# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.IntegerField()
    email = models.EmailField(blank=True)
    smtpserver = models.CharField(blank=True, max_length=255)
    smtpemail = models.CharField(blank=True, max_length=150)
    smtppassword = models.CharField(blank=True, max_length=255)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contactus = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# contact us model
class Contact(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=255)
    status = models.CharField(max_length=25, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=25)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + '_' + self.last_name


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        labels = {
            'first_name':'','last_name':'','email':'','subject':'','message':'',

        }

        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name','label':'None'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Write your message','rows':4}),
        }

