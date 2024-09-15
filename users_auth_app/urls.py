from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path(
        "password_change_with_old/",
        views.password_change_with_old,
        name="pass_change_with_old",
    ),
    path("password_change/", views.password_change, name="pass_change"),
    path("profile/", views.profile, name="profile"),
]
