from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cats/', views.cats_index, name='index'),
  path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
]