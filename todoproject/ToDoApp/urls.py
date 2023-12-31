from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.TaskListview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>', views.TaskDetail.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdate.as_view(), name='cbvupdate'),

]
