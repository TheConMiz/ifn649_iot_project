from . import views
from django.urls import path



urlpatterns = [
    path("", views.getProcessedData, name="home"),
    path("settings", views.getSettings, name="settings"),
    path("api/trends/temperature", views.getTemperatureTrends, name="temperature_trends_data"),
    path("api/trends/humidity", views.getHumidityTrends, name="humidity_trends_data"),
    path("api/trends/air_quality", views.getAirQualityTrends, name="air_quality_trends_data"),

    path("trends", views.getTrendsPage, name="trends"),
]
