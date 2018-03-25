"""thefencing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('fencing/', views.fencing_history, name='fencing_history'),
    path('fencing/events/', views.fencing_events, name='fencing_events'),
    path('fencing/clubs/', views.fencing_club, name='fencing_club'),
    path('contact/', views.contact, name='contact'),
]
