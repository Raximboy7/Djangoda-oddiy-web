from django.urls import path
from .views import HomPageView

urlpatterns = [
    path('',HomPageView.as_view(),name='home'),
]