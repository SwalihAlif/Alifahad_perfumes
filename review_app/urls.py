from django.urls import path
from .views import submit_review

urlpatterns = [
    # Other URL patterns...
    path('submit-review/', submit_review, name='submit_review'),
]
