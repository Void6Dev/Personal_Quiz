from django.urls import path
from . import views


urlpatterns = [
    path('session/create/', views.session_create_view, name='session_create'),
    path('session/join/', views.join_session_by_code, name='join_session_by_code'),
    path('session/<int:session_id>/', views.session_waiting_room, name='session_waiting'),
    path('session/<int:session_id>/players/', views.get_session_players, name='get_session_players'),
    path('session/<int:session_id>/kick/', views.kick_player, name='kick_player'),
    path('session/<int:session_id>/start/', views.session_start, name='session_start'),
    path('session/<int:session_id>/play/', views.session_play, name='session_play'),
    path('session/<int:session_id>/results/', views.session_results, name='session_results'),
    ]