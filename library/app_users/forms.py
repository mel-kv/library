from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  )
        labels = {
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Repeat password'),
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'date_of_birth' : 'date_of_birth'

        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        return user


class UserChangeForm(SignUpForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserModel
        fields = ('email', 'password', 'first_name', 'last_name', 'date_of_birth')
