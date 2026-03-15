from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ideas/', views.idea_list, name='idea_list'),
    path('ideas/create/', views.idea_create, name='idea_create'),
    path('ideas/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('ideas/<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    
    path('pipeline/', views.pipeline, name='pipeline'),
    path('pipeline/update-status/', views.update_content_status, name='update_content_status'),
    path('calendar/', views.calendar_view, name='calendar'),
    
    path('media/', views.media_library, name='media_library'),
    path('media/upload/', views.media_upload, name='media_upload'),
]
