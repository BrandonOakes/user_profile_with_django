from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .models import Profile, User
from django.core import validators
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator


class ProfileForm(forms.ModelForm):
    """creates form for user to fill in profile data"""


    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'confirm_email', 'date_of_birth', 'bio', 'avatar')

    def clean_bio(self):
        """validates that bio field is greater than 10 characters"""

        bio = self.cleaned_data['bio']
        if len(bio) < 10:
            raise forms.ValidationError("Bio must contain at least 10 characters")
        return bio

    def clean(self):
        """validates that email and confirm email fields match"""

        email = self.cleaned_data.get('email', None)
        confirm_email = self.cleaned_data.get('confirm_email', None)
        if email and confirm_email and (email == confirm_email):
            return self.cleaned_data
        else:
            raise forms.ValidationError("Emails don't match")


def min_length(value):
    """validates that password is atleast 14 characters long"""

    if len(value) < 14:
        raise forms.ValidationError("Password must be 14 characters long")


def password_case(value):
    """validates that password has one lower case and one upper case character"""

    lowercheck = []
    uppercheck = []
    for let in value:
        try:
            if let == let.lower():
                lowercheck += '1'
            elif let == let.upper():
                uppercheck += '1'
        except TypeError:
            pass
    if len(lowercheck) < 1 or len(uppercheck) < 1:
        raise forms.ValidationError("Password must contain atleast one upper and lower case letter")


def numerical_digits(value):
    """validates that password contains atleast one number"""

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digit_check = []
    for let in value:
        if let in numbers:
            digit_check += '1'
    if len(digit_check) < 1:
        raise forms.ValidationError("Password must contain atleast one numberical digit")


def special_character(value):
    """validates that password contains atleast one special character"""

    spec_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]
    character_check = []
    for let in value:
        if let in spec_characters:
            character_check += '1'
    if len(character_check) < 1:
        raise forms.ValidationError("Password must contain atleast one speacial character, example (!, @, #)")


class MyPasswordChangeForm(PasswordChangeForm):
    """form that allows user to change current password"""

    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput(),
                   validators=[min_length, password_case, numerical_digits, special_character, UserAttributeSimilarityValidator])
    new_password2 = forms.CharField(widget=forms.PasswordInput(),
                   validators=[min_length, password_case, numerical_digits, special_character, UserAttributeSimilarityValidator])

    class Meta:
        model = User


class MyUserCreationForm(UserCreationForm):
    """form that creates user and allows user to save password for username"""
    password1 = forms.CharField(widget=forms.PasswordInput(),
                 validators=[min_length, password_case, numerical_digits, special_character, UserAttributeSimilarityValidator])
    password2 = forms.CharField(widget=forms.PasswordInput(),
                 validators=[min_length, password_case, numerical_digits, special_character, UserAttributeSimilarityValidator])

    class Meta:
        model = User
        fields = ("username",)
