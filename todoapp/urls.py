from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("register/", views.register, name='register'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("create/", views.create, name='create'),
    path("create/project", views.create_project, name='create_project'),
    path("create/task", views.create_task, name='create_task'),
]
