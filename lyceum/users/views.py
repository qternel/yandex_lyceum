import django.contrib.auth.views as admin_views
from catalog.models import Item, Tag
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from rating.models import Rating

from users.forms import ProfileForm, UserForm, UserLoginForm, UserRegistrationForm
from users.models import Profile


def user_list(request):
    TEMPLATE = 'users/user_list.html'
    users = User.objects.all().prefetch_related(
        Prefetch('profile', queryset=Profile.objects.all())
    )

    context = {'users': users}
    return render(request, TEMPLATE, context)


def user_detail(request, pk):
    TEMPLATE = 'users/user_detail.html'
    user = get_object_or_404(User.objects.only(
        'email', 'first_name', 'last_name', 'profile__birthday'
    ).select_related('profile'), pk=pk)
    liked_items = Item.objects.filter(
        pk__in=Rating.objects.filter(
            user=user, star=5).values_list('item_id')
    ).prefetch_related(
        Prefetch('tags', queryset=Tag.objects.published_tags())
    ).only('name', 'text', 'tags__name', 'category_id')
    context = {'user': user,
               'items': liked_items}
    return render(request, TEMPLATE, context)


def signup(request):
    TEMPLATE = 'users/signup.html'

    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return redirect('login')

    context = {'form': form}
    return render(request, TEMPLATE, context)


def profile(request):
    TEMPLATE = 'users/profile.html'
    liked_items = Item.objects.filter(
        pk__in=Rating.objects.filter(
            user=request.user, star=5).values_list('item_id')
    ).prefetch_related(
        Prefetch('tags', queryset=Tag.objects.published_tags())
    ).only('name', 'text', 'tags__name', 'category_id')

    user_form = UserForm(request.POST or None, instance=request.user)
    profile_form = ProfileForm(
        request.POST or None, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect('profile_page')
    context = {
        'items': liked_items,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, TEMPLATE, context)


def login_page(request):
    TEMPLATE = 'users/login.html'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data_cleaned = form.cleaned_data
        user = authenticate(username=data_cleaned['username'], password=data_cleaned['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile_page')
            else:
                form.add_error(None, 'Аккаунт неактивиен')
        else:
            form.add_error(None, 'Пользователь не найден')

    context = {'form': form}
    return render(request, TEMPLATE, context)


class LoginView(admin_views.LoginView):
    template_name = 'users/login.html'


class PasswordChangeDoneView(admin_views.PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class LogoutView(admin_views.LogoutView):
    template_name = 'users/logout.html'


class PasswordResetView(admin_views.PasswordResetView):
    template_name = 'users/password_reset.html'


class PasswordResetDoneView(admin_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(admin_views.PasswordResetConfirmView):
    template_name = 'users/reset.html'


class PasswordResetCompleteView(admin_views.PasswordResetCompleteView):
    template_name = 'users/reset_done.html'


class PasswordChangeView(admin_views.PasswordChangeView):
    template_name = 'users/password_change.html'
