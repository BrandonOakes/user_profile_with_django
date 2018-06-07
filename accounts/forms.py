from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile, User




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


# class UserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2")
#         help_texts = {
#             'username':'sup',
#             'email': None,
#         }
#
#         def clean_password(self):
#             password = self.cleaned_data['password']
#             special_characters =['!', '@', '#', '$', '%', '^', '&', '*']
#             if len(password) < 14:
#                 raise forms.ValidationError("password must be at least 14 characters long")
#             elif sum(num.isdigit() for num in password) < 1:
#                 raise forms.ValidationError("password must contain 1 number")
#             elif not any(let.isupper() for let in password) < 1:
#                 raise forms.ValidationError("password must contain at least 1 uppercase letter")
#             elif not any(let.islower() for let in password) < 1:
#                 raise forms.ValidationError("password must contain at least 1 lowercase letter")
#             elif not any(special_characters for let in password) <1:
#                 raise forms.ValidationError("password must contain atleast 1 special character such as !, @, # etc ")
#             else:
#                 return password
