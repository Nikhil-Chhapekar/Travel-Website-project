from django.urls import path
from . import views

urlpatterns = [
    path('destination/<slug:destination_slug>/add/', views.add_destination_review, name='add_destination_review'),
    path('destination/<slug:destination_slug>/edit/<int:review_id>/', views.edit_destination_review, name='edit_destination_review'),
    path('destination/<slug:destination_slug>/delete/<int:review_id>/', views.delete_destination_review, name='delete_destination_review'),
    path('accommodation/<int:accommodation_id>/add/', views.add_accommodation_review, name='add_accommodation_review'),
    path('activity/<int:activity_id>/add/', views.add_activity_review, name='add_activity_review'),
    path('my-reviews/', views.my_reviews, name='my_reviews'),
]
