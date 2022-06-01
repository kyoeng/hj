from django.urls import path
from . import views

app_name                                      = 'board'
urlpatterns                                   = [
    path('', views.IndexView.as_view()),
    path('write/', views.WriteView.as_view())
]