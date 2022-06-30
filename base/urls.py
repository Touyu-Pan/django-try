from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # passing a dynamic value to an url
    path('room/<str:pk>/', views.room, name="room"),
]