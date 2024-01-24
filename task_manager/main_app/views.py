from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

def index(request):
    return HttpResponse("fjdklmsc;,a./x~")
# Create your views here.
def main_page(request):
    return render(request, 'main_app/main_page.html')
def my_profile(request):
    return render(request, 'main_app/my_profile.html', {'user': request.user})
def add_task(request):
    if not request.user.is_authenticated:
        return render(request, 'main_app/login.html', {'error_message': 'Сначала зарегистрируйтесь!'})
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.user_id = request.user.id
            task.save()
            return redirect('main_page') #
        else:
            return redirect('my_profile')
    else:
        #print(2)
        form = TaskForm()
    return render(request, 'main_app/add_task.html', {'form': form})
def task_info(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'main_app/task_info.html', context={'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    #print(1)task_id
    return redirect('main_page')
def my_tasks(request):
    elements = Task.objects.filter(user=request.user.id)
    return render(request, 'main_app/my_tasks.html',{"els" : elements})

def register(request):
    if request.user.is_authenticated:
        return redirect('my_profile')
    else:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                return redirect('my_profile')
        else:
            user_form = UserRegistrationForm()
        return render(request, 'main_app/reg.html', {'user_form': user_form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('my_profile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            error_message = 'Пользователь не найден'
            return render(request, 'main_app/login.html', {'error_message': error_message})
    else:
        return render(request, 'main_app/login.html')

def logout_view(request):
    if not request.user.is_authenticated:
        return render(request, 'main_app/login.html', {'error_message': 'Сначала зарегистрируйтесь!'})
    logout(request)
    return redirect('main_page')
