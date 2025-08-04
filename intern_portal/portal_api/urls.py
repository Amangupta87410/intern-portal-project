from django.urls import path
from .views import intern_data, leaderboard_data

urlpatterns = [
    path('data/', intern_data, name='intern-data'),
    path('leaderboard/', leaderboard_data, name='leaderboard-data'),
]