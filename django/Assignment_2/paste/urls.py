from django.urls import path
from django.conf.urls import url
from django_filters.views import FilterView
from .filters import PostFilter
from . import views
from .views import (
	PostListView, PostDetailView, 
	PostCreateView, PostUpdateView, 
	PostDeleteView, UserPostListView, PostUploadView)

urlpatterns = [
	path('', PostListView.as_view(), name='paste-home'),
	path('about/', views.about, name='paste-about'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
	path('post/newupload', PostUploadView.as_view(), name='post-upload'),

	url(r'post/search/', FilterView.as_view(filterset_class=PostFilter,
        template_name='paste/post_list.html'), name='search'),
]
