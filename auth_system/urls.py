from auth_system import views
from django.urls import path
urlpatterns = [
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login'),
    path('login/', views.logout_page, name='logout')
]