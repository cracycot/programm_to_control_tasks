from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', main_page, name = 'main_page'),
     path('tasks/', my_tasks, name = 'my_tasks'),
     path('my_profile/', my_profile, name = 'my_profile'),
     path('add_task/', add_task, name = 'add_task'),
     path('registration/', register, name = 'reg'),
     path('login/',login_view, name='login'),
     path('logout/',logout_view, name='logout'),

     path('delete_task/', delete_task, name='delete_task'),
     path('task/<int:task_id>/', task_info, name = 'task_info')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
