from django.urls import path

from . import views
from .views import user_detail

urlpatterns = [
    path('notes/', views.get_notes),  # localhost:8000/api/notes/
    path('notes/new/', views.create_note),
    path('notes/<uuid:id>/', views.note_detail),
    path('users/<int:id>/', user_detail, name='user-detail'),

    path('users/', views.get_users),  # localhost:8000/api/users/

]
