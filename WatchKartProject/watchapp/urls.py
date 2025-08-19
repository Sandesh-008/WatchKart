from django.urls import path
from .views import add_watch, display_watch, update_watch, delete_watch

urlpatterns=[
    path('add_watch/', add_watch, name='add-watch'),
    path('display_watch/', display_watch, name='display-watch'),
    path('update_watch/<id>/', update_watch, name='update-watch'),
    path('delete_watch/<id>/', delete_watch, name='delete-watch'),
]