from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # List all posts
    path('', views.PostListView.as_view(), name='post_list'),

    # View single post
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # Create new post
    path('new/', views.PostCreateView.as_view(), name='post_create'),

    # Edit existing post
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),

    # Delete post
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
