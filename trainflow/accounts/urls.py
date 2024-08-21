from django.urls import path

from .views import signup, login_user, logout_user, info, switch_profile, athlete_signup, delete_account

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login_user, name='login'),
    path('info', info, name='info'),
    path('logout', logout_user, name='logout'),
    path('switch-profile', switch_profile, name='switch-profile'),
    path("athlete-signup", athlete_signup, name="athlete-signup"),
    path("delete-account", delete_account, name="delete-account")
]
