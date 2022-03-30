from . import views
from django.urls import path

urlpatterns = [
    path('', views.fun1, name='fun1'),
    path('delete/<int:id>/', views.done, name='done'),
    path('update/<int:tid>/', views.update, name='update')

]
