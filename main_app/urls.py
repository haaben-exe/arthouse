from django.urls import path
from . import views


urlpatterns = [
    path('', 
         views.LandingPage, 
         name='landing'
         ),

    path(
        'home/', 
        views.HomePage, 
        name='home'
        ),

    path(
        'post/create/', 
        views.CreatePost.as_view(), 
        name='post_create'
        ),

    path(
        'post/<int:post_id>/', 
        views.PostPage, 
        name='post_detail'
        ),

    path(
        'post/<int:pk>/update/', 
        views.PostUpdate.as_view(), 
        name='post_update'
        ),

    path(
        'post/<int:pk>/delete/', 
        views.PostDelete.as_view(), 
        name='post_delete'
        ),

    path(
        'search/', 
        views.SearchPage, 
        name='search_page'
        ),

    path(
        'profile/', 
        views.ProfilePage, 
        name='profile'
        )
]