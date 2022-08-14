from django.urls import path
from portfolioapp.apps import PortfolioappConfig
from portfolioapp import views

app_name = PortfolioappConfig.name

urlpatterns = [
    path('', views.home, name='home'),
]

