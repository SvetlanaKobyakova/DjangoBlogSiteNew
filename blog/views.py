from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


def index(request):
    # получение всех постов, отсортированных по дате публикации (select * from blog_post, order by create_at DESK)
    posts = Post.objects.all().order_by('-created_at')
    count_posts = Post.objects.count()
    # показываем по три поста на странице
    per_page = 3
    paginator = Paginator(posts, per_page)
    # получаем номер страницы из URL
    page_number = request.GET.get('page')
    # получаем объекты для текущей страницы
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Главная страница',
               'page_obj': page_obj,
               'count_posts': count_posts
               }
    return render(request, template_name='blog/index.html', context=context)


def about(request):
    count_posts = Post.objects.count()
    context = {'title': 'О сайте', 'count_posts': count_posts}
    return render(request, template_name='blog/about.html', context=context)

@login_required
def add_post(request):
    if request.method == "GET":
        post_form = PostForm(author=request.user)
        context = {'title': "Добавить пост",'form':post_form}
        return render(request, template_name='blog/post_add.html', context=context)

    if request.method == "POST":
        post_form = PostForm(data=request.POST, files=request.FILES, author=request.user)
        if post_form.is_valid():
            post_form.save()
            return index(request)
        return None
    return None


def read_post(request, slug):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, slug=slug)
    context = {'title': "Информация о посте", 'post': post}
    return render(request, template_name='blog/post_detail.html', context=context)

@login_required
def update_post(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.author = post_form.cleaned_data['author']
            post.image = post_form.cleaned_data['image']
            post.save()
            return redirect("blog:read_post", slug=post.slug)
    else:
        post_form = PostForm(initial={
            "title": post.title,
            "author": post.author,
            "text": post.text,
            "image": post.image,
        })
        return render(request, template_name="blog/post_edit.html", context={"form": post_form})

@login_required
def delete_post(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    if request.method == "POST":
        post.delete()
        return redirect('blog:index')
    return render(request, template_name='blog/post_delete.html', context=context)


def page_not_found(request, exception):
    return render(request, template_name='blog/404.html', context={'title': '404'})


def forbidden(request, exception):
    return render(request, template_name='blog/403.html', context={'title': '403'})


def server_error(request):
    return render(request, template_name='blog/500.html', context={'title': '500'})