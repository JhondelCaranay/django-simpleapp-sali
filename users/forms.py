from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
# import Q from django
from django.db.models import Q


class SignUpForm(UserCreationForm):
    # username = forms.CharField(

    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Username',
    #         }
    #     ),
    #     required=True,
    # )

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     ),
    #     max_length=30, required=True)

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     ),
    #     max_length=30, required=True)  # , help_text='Optional.'
    # email = forms.EmailField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     ),
    #     max_length=254, help_text='Required. Inform a valid email address.')

    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     ),
    #     required=True,
    #     max_length=30,
    #     label='Password',
    # )

    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     ),
    #     required=True,
    #     max_length=30,
    #     label='Confirm password',
    # )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2',
        )

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field in self.fields:

            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                    # 'placeholder': self.fields[field].label,
                    # 'required': True
                }
            )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            # both are the same , will display in {{ form.name_of_field.errors }}
            # self.add_error('username', 'Username already exists')
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError('Email is required')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email

    # def clean(self):
    #     cleaned_data = super(SignUpForm, self).clean()
    #     username = cleaned_data.get('username')

    #     if User.objects.filter(username=username).exists():
    #         # this will display in {{ form.name_of_field.errors }}
    #         self.add_error('username', 'Username already exists')
    #         # this will display in form.non_field_errors
    #         raise forms.ValidationError('Username already exists awol')

    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']

    #     if commit:
    #         user.save()
    #     return user

        # password1 = cleaned_data.get('password1')
        # password2 = cleaned_data.get('password2')
        # if password1 != password2:
        #     raise forms.ValidationError('Passwords do not match')
        # return cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['first_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['last_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs.update(
    #         {
    #             'class': 'form-control',
    #             'placeholder': self.fields['password2'].label,
    #             'required': True
    #         })


# class SignUpForm(forms.Form):
#     username = forms.CharField(
#         max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True
#     )

#     first_name = forms.CharField(
#         max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True
#     )

#     last_name = forms.CharField(
#         max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True
#     )

#     email = forms.EmailField(
#         max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True
#     )
#     password = forms.CharField(
#         max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True
#     )
#     confirm_password = forms.CharField(
#         max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True
#     )


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, label='Username or Email'
    )
    password = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True
    )

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     user = User.objects.filter(Q(username=username) | Q(email=username))

    #     if not user.exists():
    #         raise forms.ValidationError('Username or Email does not exist')
    #     return username

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = User.objects.filter(Q(username=username) | Q(email=username))

        if not user.exists():
            self.add_error('username', 'Username or Email does not exist')

        if user.exists() and not user.first().check_password(password):
            self.add_error('password', 'Password is incorrect')

        return cleaned_data


class SignInForm2(AuthenticationForm):
    # username = forms.CharField(
    #     max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, label='Username or Email'
    # )
    # password = forms.CharField(
    #     max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True
    # )

    # make it possible to login with username and email
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = None

        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except User.DoesNotExist:
            self.add_error('username', 'username or email does not exists')

        if user and password:
            self.user_cache = authenticate(
                username=user.username, password=password)
            if self.user_cache is None:
                self.add_error('password', 'Password is incorrect')
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(SignInForm2, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Username or Email'

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                    # 'placeholder': self.fields[field].label,
                    # 'required': True
                }
            )
