from django.urls import include, path
from django.contrib.auth.views import (
    LogoutView,
)
from .views import (
    index,
    login_user,
    Dashboard,
)


app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", login_user, name="login"),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
