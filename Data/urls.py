from django.urls import path
from .views import HomeView, EditView, DeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('edit/<int:pk>/', EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
]
