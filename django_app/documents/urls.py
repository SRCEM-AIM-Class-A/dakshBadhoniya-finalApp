from django.urls import path
from .views import document_list_view

app_name = 'documents'

urlpatterns = [
    path('', document_list_view, name='list'),
]
