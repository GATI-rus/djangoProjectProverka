from django.contrib import admin
from django.urls import path
from proverka import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('finihs/', views.finish, name='finish'),
    path('form/1/', views.formcomment, name='forma1'),
    path('form/2/', views.formtel, name='forma2'),
]
