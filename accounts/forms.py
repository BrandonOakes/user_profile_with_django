from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .models import Profile, User
from django.core import validators
import pdb





class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'confirm_email', 'date_of_birth', 'bio', 'avatar')


    def clean_bio(self):
        bio = self.cleaned_data['bio']
        if len(bio) < 10:
            raise forms.ValidationError("Bio must contain at least 10 characters")
        return bio

    def clean(self):
        email = self.cleaned_data.get('email', None)
        confirm_email = self.cleaned_data.get('confirm_email', None)
        if email and confirm_email and (email == confirm_email):
            return self.cleaned_data
        else:
            raise forms.ValidationError("Emails don't match")


# Validates that the "current password" is correct",
#  "new password" and "confirm password" fields match,
#  and follows the password policy:

# must not be the same as the current password
# def different_password(value):
#     current_password = request.user.password
#     if value == current_password:
#         raise forms.ValidationError("new password can not match current password")



# minimum password length of 14 characters.
def min_length(value):
    if len(value) < 14:
        raise forms.ValidationError("Password must be 14 characters long")

# must use of both uppercase and lowercase letters
def password_case(value):
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



# must include one or more numerical digits
def numerical_digits(value):
    # pdb.set_trace()
    numbers= ['0','1','2','3','4','5','6','7','8','9']
    digit_check = []
    for let in value:
        if let in numbers:
            digit_check += '1'
    if len(digit_check) < 1:
        raise forms.ValidationError("Password must contain atleast one numberical digit")


# must include one or more of special characters, such as @, #, $

def special_character(value):
    spec_characters= ["!", "@", "#", "$", "%", "^", "&", "*", "?"]
    character_check = []
    for let in value:
        if let in spec_characters:
            character_check += '1'
    if len(character_check) < 1:
        raise forms.ValidationError("Password must contain atleast one speacial character, example (!, @, #)")

# cannot contain the user name or parts of the user’s full name, such as their first name


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput(), validators=[ min_length, password_case, numerical_digits, special_character])
    new_password2 = forms.CharField(widget=forms.PasswordInput(), validators=[ min_length, password_case, numerical_digits, special_character])
    class Meta:
        model = User
