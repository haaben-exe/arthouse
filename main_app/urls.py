from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', 
         views.LandingPage.as_view(), 
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
        ),

    path(
        'login/', 
        views.Login, 
        name='signup'
        ),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
