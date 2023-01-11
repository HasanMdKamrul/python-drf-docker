
from django.contrib import admin
from django.urls import include, path
from posts.views import Create_post, Destroy_post, Get_all_posts, Retrive_post

# from posts.views import get_all_posts, get_post_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/posts/', Get_all_posts.as_view(), name='posts'),
    path('api/posts/create/', Create_post.as_view(), name='create-post'),
    path('api/posts/<pk>/', Retrive_post.as_view(), name='posts-detail'),
    path('api/posts/<pk>/delete', Destroy_post.as_view(), name='posts-detail'),
    # path('api/posts/<int:pk>/', PostListMixinView.as_view(), name='posts-detail'),
    # path('api/posts/<int:pk>/', Postview.as_view(), name='posts'),
    # path('api/posts/', get_all_posts, name="all-posts"),
    # path('api/posts/<int:pk>/', get_post_detail, name='post_detail'),
    # path('posts/', Postview.as_view(), name='posts'),
    # path('api/posts/', post_list, name='post_list'),
    # path('api/posts/<int:pk>/', post_detail, name='post_detail'),
]
