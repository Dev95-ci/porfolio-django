from django.urls import path
from .views import ProjectListView, ProjectDetailView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dev95-Porfolio/about/', views.about, name='about'),
    path('dev95-Porfolio/contact/', views.contact, name='contact'),
    path('dev95-Porfolio/project', ProjectListView.as_view(), name='project_list'),  # Liste des projets
    path('dev95-Porfolio/projet/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),  # Détails d'un projet
]
