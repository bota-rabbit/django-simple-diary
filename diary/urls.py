from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
