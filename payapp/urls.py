from django.urls import path

from payapp.views import views
from payapp.views.home import Home

urlpatterns = [
    # path('', views.index, name='index'),
    path('', Home.as_view()),
]
