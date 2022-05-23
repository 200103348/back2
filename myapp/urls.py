from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register),
    path('lo/', views.signin),
    path('in/', views.page),
    path('', views.newproject, name='project'),
    path('news/', views.form, name='sportnews'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:id>/delete', views.delete, name='news-delete'),
    path('olympics/', views.olympics, name='olympics'),
    path('tokyo/', views.tokyo),
    path('news_home/', views.news_home, name='add-post'),
    path('post/<slug:post_id>', views.show_post, name='post'),
]