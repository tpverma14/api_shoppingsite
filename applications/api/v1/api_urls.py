from django.urls import path, include
from api.v1.apiview.blog_view import PostListApiView, PostDetailAPIView \
    , PostUpdateAPIView, PostDeleteAPIView,  PostCreateAPIView \
    ,CommentDetailsApiView ,CommentListApiView \
    ,BlogCommentApiView ,CommentCreateApiView

app_name='blog-api'

urlpatterns = [
    path('blog_list/',PostListApiView.as_view(),name='list'),
    path('blog_detail/<slug:slug>/',PostDetailAPIView.as_view(),name='detail'),
    path('blog_update/<slug:slug>/', PostUpdateAPIView.as_view(),name='update'),
    path('blog_delete/<slug:slug>/', PostDeleteAPIView.as_view(),name='delete'),
    path('blog_create/', PostCreateAPIView.as_view(),name='create'),
    path('comment_detail/<slug:id>/', CommentDetailsApiView.as_view(),name='comment_detail'),
    path('comment_list/', CommentListApiView.as_view(),name='comment_list'),
    path('blogcomment_list/<slug:id>/', BlogCommentApiView.as_view(),name='blogcomment_list'),
    path('comment_create/<slug:slug>/', CommentCreateApiView.as_view(),name='comment_create'),
]
