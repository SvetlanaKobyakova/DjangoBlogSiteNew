from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    # получение всех постов (select * from blog_post)
    posts = Post.objects.all()
    context = {'title': 'Главная страница', 'posts': posts}
    return render(request, template_name='blog/index.html', context=context)

def about(request):
    context = {'title': 'О сайте'}
    return render(request, template_name='blog/about.html', context=context)

def add_post(request):
    if request.method == "GET":
        post_form = PostForm()
        context = {'title': "Добавить пост",'form':post_form}
        return render(request, template_name='blog/post_add.html', context=context)

    if request.method == "POST":
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post = Post()
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.author = post_form.cleaned_data['author']
            post.image = post_form.cleaned_data['image']
            post.save()
            return index(request)

def read_post(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'title': "Информация о посте", 'post': post}
    return render(request, template_name='blog/post_detail.html', context=context)

def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.author = post_form.cleaned_data['author']
            post.image = post_form.cleaned_data['image']
            post.save()
            return redirect("blog:read_post", pk=post.id)
    else:
        post_form = PostForm(initial={
            "title": post.title,
            "author": post.author,
            "text": post.text,
            "image": post.image,
        })
        return render(request, template_name="blog/post_edit.html", context={"form": post_form})