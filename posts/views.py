from django.shortcuts import render, redirect
# from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm
from .models import Post

# from class base view imports
from django.views import View
from django.utils.decorators import method_decorator
# paginator
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

# @login_required(login_url='sign_in')


@login_required
def create_post(request):
    form = PostCreationForm()

    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            # form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'posts/create_post.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostCreationForm(instance=post)

    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'posts/update_post.html', context)


""" CLASS BASE VIEW """


class HomePageView(View):

    template_name = 'posts/index.html'

    def get(self, request):
        posts = Post.objects.all()

        # pagination
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'posts': page_obj
        }
        return render(request, self.template_name, context)
        # return render(request, 'posts/index.html', context)


class AboutPageView(HomePageView):

    template_name = 'about.html'


@method_decorator(login_required, name='dispatch')  # method 3
class CreatePostView(View):
    template_name = 'posts/create_post.html'

    # method 1
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('sign_in')
    #     return super().dispatch(request, *args, **kwargs)

    #  method 2
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = PostCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = PostCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)
