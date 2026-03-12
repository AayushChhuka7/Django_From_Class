from django.urls import path
from .views import StudentLoginView

urlpatterns = [
    # path('register/', RegistrationView.as_view(), name='register'),
    path('login/', StudentLoginView.as_view(), name='student-login'),
]