from django.urls import path, include
from .views import auth_view

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', auth_view, name='authView'),
]
