
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import index, about, services, create_post,  post_detail, update_post, HomePageView, AboutPageView, CreatePostView

urlpatterns = [
    # path('', index, name='home'),
    # path('about/', about, name='about'),
    path('services/', services, name='services'),
    # path('post/create/', create_post, name='create_post'),
    path('post/detail/<int:id>', post_detail, name='post_detail'),
    path('post/update/<int:id>', update_post, name='update_post'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/create/', CreatePostView.as_view(), name='create_post'),
]

# HOW TO ADD LOGIN REQUIRED TO CLASS BASE VIEW (METHOD 4)
# https://stackoverflow.com/questions/60871630/login-required-decorator-on-a-class-based-view-in-django
