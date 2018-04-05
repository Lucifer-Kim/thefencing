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
    path('', views.index, name='index'),
    path('fencing/', views.fencing_history, name='fencing_history'),
    path('fencing/events/', views.fencing_events, name='fencing_events'),
    path('fencing/rules/', views.fencing_rules, name='fencing_rules'),
    path('fencing/terms/', views.fencing_terms, name='fencing_terms'),
    path('fencing/clubs/', views.fencing_club, name='fencing_club'),
    path('media/news/', views.media_news, name='media_news'),
    path('media/forum/', views.fencing_forum, name='fencing_forum'),
    path('media/photo/', views.fencing_photo, name='fencing_photo'),
    path('media/photo/', views.fencing_video, name='fencing_video'),
    path('square/freeboard/', views.free_board, name='free_board'),
    path('square/freeboard/write/', views.write_free_board, name='write_free_board'),
    path('square/qnaboard/', views.qna_board, name='qna_board'),
    path('square/fleamarket/', views.fleamarket, name='fleamarket'),
    path('update/', views.update, name='update'),
    path('contact/', views.contact, name='contact'),
]
