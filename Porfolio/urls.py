from django.urls import path
from .views import ProjectListView, ProjectDetailView
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='home'),
    path('dev95-Porfolio/about/', views.about, name='about'),
    path('dev95-Porfolio/contact/', views.contact, name='contact'),
    path('dev95-Porfolio/project', ProjectListView.as_view(), name='project_list'),  # Liste des projets
    path('dev95-Porfolio/projet/<int:project_id>/', views.project_detail, name='project_detail'),  # Détails d'un projet
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
