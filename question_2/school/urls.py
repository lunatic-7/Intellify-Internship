from django.urls import path
from . import views

urlpatterns = [
    # Main Home Page
    path('', views.home, name="home"),
    # Contact Page
    path('contact/', views.contact, name="contact"),
    # Student Profile View Page
    path('student/', views.student, name="student"),
    # Teacher Profile View Page
    path('teacher/', views.teacher, name="teacher"),
    # Student Registration Page
    path('sregister/', views.sregister, name="sregister"),
    # Teacher Registration Page
    path('tregister/', views.tregister, name="tregister"),
    # Common Login Page
    path('login/', views.handleLogin, name="handleLogin"),
    # Common Logout Page
    path('logout/', views.handleLogout, name='handleLogout'),
]
