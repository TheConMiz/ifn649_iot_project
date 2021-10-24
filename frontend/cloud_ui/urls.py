from . import views
from django.urls import path



urlpatterns = [
    path("", views.getProcessedData, name="home"),
    path("settings", views.getSettings, name="settings"),
    path("api/trends", views.getTrends, name="trends_data"),
    path("trends", views.getTrendsPage, name="trends"),
]
