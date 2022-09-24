from django.urls import path
from portfolioapp.apps import PortfolioappConfig
from portfolioapp import views

app_name = PortfolioappConfig.name

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='home'),
    path('<int:pk>/detail/', views.ProjectDetailView.as_view(), name='project_detail')
]

