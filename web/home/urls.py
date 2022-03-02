from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path ("", views.landing, name ="index"),
    path ("login", views.login_view, name = "login"),
    path ("logout", views.logout_view, name = "logout"),
    path ("newsfeed", views.newsfeed, name = "newsfeed"),
    path ("games", views.games, name ="games"),
    path ("chat", views.chat, name ="chat"),
    path ("posting", views.posting, name = "posting"),
    path ("posts", views.posts, name = "posts"),
    path ("signup", views.signup_view, name = "signup"),
    path ("landing", views.landing, name = "landing"),
    path ("userpage", views.userpage, name = "userpage"),
]