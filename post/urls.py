from django.urls import path
from . import views
app_name = 'post'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.add, name = 'add'),
    path('<int:post_id>/', views.details, name='detail'),
    path('<int:post_id>/update', views.update, name='update')
]
