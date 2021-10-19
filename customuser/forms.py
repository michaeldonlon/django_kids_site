# customuser/forms.py
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import (
        ReadOnlyPasswordHashField, 
        AuthenticationForm
)
from django.core.exceptions import ValidationError
from django.forms import (
    ModelForm,
    CharField,
    EmailField,
    TextInput,
    PasswordInput
)


class CustomUserCreateForm(ModelForm):

    password1 = CharField(
        label='Password',
        min_length=8,
        widget=PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = CharField(
        label='Password confirmation',
        min_length=8,
        widget=PasswordInput,
        help_text=("<br>Please repeat the password for verification."),
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the entered passwords match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        # Save the password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
        )


class LoginForm(AuthenticationForm):
    username = EmailField(
        label='Email', 
        widget=TextInput(attrs={'autofocus': True})
    )
