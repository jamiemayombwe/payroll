from django.urls import path

from payapp.views.home import Home
from payapp.views.login import Login, Logout

urlpatterns = [
    # path('', views.index, name='index'),
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
