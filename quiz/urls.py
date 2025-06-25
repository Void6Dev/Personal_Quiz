from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.quiz_list_view, name="main_page"),
    path('quiz-creation/', views.quiz_create_view, name="quiz_creation"),
    path('quiz/<int:id>/', views.quiz_detail_view, name='quiz_detail'),
]