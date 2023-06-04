from django.urls import path

from core import views

# ----------------------------------------------------------------------------------------------------------------------
# Create Core app urls
urlpatterns: list = [
    path("signup", views.UserSignupView.as_view(), name="user-signup"),
    path("login", views.UserLoginView.as_view(), name="user-login"),
    path("profile", views.UserRetrieveUpdateDestroyView.as_view(), name="user-profile"),
]
