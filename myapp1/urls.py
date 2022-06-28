from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('home/', views.home, name='home'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('availablejobs/', views.availablejobs, name='availablejobs'),
    path('appliedjobs/', views.appliedjobs, name='appliedjobs'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('developer/', views.developer, name='developer'),
    

    
]