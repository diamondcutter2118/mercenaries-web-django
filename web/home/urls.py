from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path ("", views.index, name ="index"),
    path ("login", views.login_view, name = "login"),
    path ("logout_view", views.logout_view, name = "logout"),
    path ("newsfeed", views.newsfeed, name = "newsfeed"),
    path ("games", views.games, name ="games"),
    path ("chat", views.chat, name ="chat"),
    path ("posting", views.posting, name = "posting"),
    path ("posts", views.posts, name = "posts"),
    path ("signup", views.signup_view, name = "signup"),
    path ("loged_in_index", views.loged_in_index, name = "loged_in_index"),
]