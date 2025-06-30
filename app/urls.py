from django.urls import path
from .views import LoginView, IndexView, RegisterView, LogoutView, PreferencesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('preferences/', PreferencesView.as_view(), name='preferences'),
]
