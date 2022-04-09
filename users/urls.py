
from tempfile import template
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import sign_up, sign_in, sign_out
from .forms import SignUpForm, SignInForm2
urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
    path(
        'login/',
        LoginView.as_view(
            template_name='users/sign_in.html', authentication_form=SignInForm2
        ),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
