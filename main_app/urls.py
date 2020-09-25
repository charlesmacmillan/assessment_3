from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_widget/', views.WidgetCreate.as_view(), name='add_widget'),
    path('delete/<int:id>', views.delete_widget, name='delete'),
]