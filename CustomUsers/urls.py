from django.urls import path, include
from .views import (
    signup_view,
    home_view,
    login_view,
    SUview
)
from django.contrib.auth import views

app_name = 'Users'

urlpatterns = [
    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view.as_view(),  name="login"),
    path('newusers/', SUview.as_view(), name="new_users")
]