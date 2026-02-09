from django.urls import path
from .views import RegisterAPIView
from .views import login_page,register_page

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    
]