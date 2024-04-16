from django import forms
from django.core import validators
from .models import Customer

class CustomerSignInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class CustomerSignUpForm(forms.ModelForm):
    name_regex = '^[a-zA-Z ]+$'  
    username_regex = '^[a-zA-Z0-9]+$'  
    phone_regex = r'^\+?1?\d{9,15}$'
    min_length = 1
    max_length = 25
    error_message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits is allowed."
    
    validation_msg_min = "Should have at least {} characters".format(min_length)
    validation_msg_max = "Should have at most {} characters".format(max_length)

    first_name = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, message=validation_msg_min),
        validators.MaxLengthValidator(max_length, message=validation_msg_max),
        validators.RegexValidator(name_regex, message='Enter a valid first name.')
    ])
    
    last_name = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, message=validation_msg_min),
        validators.MaxLengthValidator(max_length, message=validation_msg_max),
        validators.RegexValidator(name_regex, message='Enter a valid last name.')
    ])
    
    username = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, message=validation_msg_min),
        validators.MaxLengthValidator(max_length, message=validation_msg_max),
        validators.RegexValidator(username_regex, message='Enter a valid username.')
    ])
    
    company_name = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, message=validation_msg_min),
        validators.MaxLengthValidator(max_length, message=validation_msg_max),
        validators.RegexValidator(name_regex, message='Enter a valid company name.')
    ])
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'company_name', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
