from catalog.forms import FormStyleMixin
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

