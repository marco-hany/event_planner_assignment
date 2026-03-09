from django.urls import path
from . import views

urlpatterns=[
    path('create/', views.create_event, name='create_event'),
    path('<uuid:event_id>/update/', views.update_event, name='update_event'),
    path('', views.get_all_events, name='get_all_events'),
    path('<uuid:event_id>/', views.get_event, name='get_event'),
    path('<uuid:event_id>/delete/', views.delete_event, name='delete_event'),
]