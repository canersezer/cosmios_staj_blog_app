from django.urls import path

from rest_framework.authtoken import views

from .views import CreateAPIView,logout

urlpatterns = [
    path('register/',CreateAPIView.as_view()),
    path('login/',views.obtain_auth_token),
    path('logout/',logout),
]
 