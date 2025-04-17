from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, NewRegistrationForm
from BlogSite.settings import LOGIN_REDIRECT_URL




def register(request):
    # когда отправляем заполненную форму на сервер
    if request.method == "POST":
        # создаем объект с данными из запроса
        form = NewRegistrationForm(request.POST)

        # если форма валидна, то
        if form.is_valid():
            # создаем объект пользователя без записи в БД
            new_user = form.save(commit=False)
            # хэшируем пароль при помощи set_password
            new_user.set_password(form.cleaned_data['password'])
            # сохраняем пользователя в БД
            new_user.save()
            context = {'title': 'Регистрация завершена', 'new_user': new_user}
            return render(request, template_name='users/registration_done.html', context=context)

    # если метод GET с пустой формой регистрации
    form = NewRegistrationForm()
    context = {'title': 'Регистрация пользователя', 'register_form': form}
    return render(request, template_name='users/registration.html', context=context)

def log_in(request):
    # создание формы аутентификации
    form = AuthenticationForm(request, request.POST)
    # проверка формы
    if form.is_valid():
        # получение логина и пароля из формы
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # аутентификация пользователя
        # проверка существования
        user = authenticate(username=username, password=password)
        # если такой пользователь существует и пароль верный
        if user:
            # авторизация пользователя
            login(request, user)
            # получение дальнейшего маршрута после входа на сайт
            # next - путь, откуда пришел пользователь на страницу входа
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    context = {'form': form}
    return render(request, template_name='users/login.html', context=context)

@login_required
def log_out(request):
    logout(request)
    return redirect('blog:index')

@login_required
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
        raise PermissionDenied()
    context = {'user': user, 'title': 'Информация о пользователе'}
    return render(request, template_name='users/profile.html', context=context)


