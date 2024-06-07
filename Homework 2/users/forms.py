from django import forms
from catalog.forms import FormStyleMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'avatar', 'country', 'phone')


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
