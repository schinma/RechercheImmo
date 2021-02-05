from django.urls import path

from . import views

app_name = 'immoapp'

urlpatterns = [
    path('appartements/', views.APIAppartementListView.as_view(), name='appartements'),
    path('projets/', views.APIProjetListView.as_view(), name="projet"),
    path('projets/<pk>/', views.APIProjetDetailView.as_view(), name='projets-detail'),
    path('projets/<projet_id>/create/', views.APIAppartementCreateView.as_view(), name='appartement-create'),
]