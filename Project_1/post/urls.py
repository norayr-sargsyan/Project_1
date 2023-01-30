from django.urls import path
from post.post_views import post_views

urlpatterns = [
    path("post/", post_views.PostListCreateView.as_view()),
    path("post/<int:post>/", post_views.LikeListCreateView.as_view()),
    path("post/<int:post>/", post_views.CommentListCreateView.as_view()),
    path("<int:pk>/", post_views.PostRetrieveUpdateDestroyView.as_view()),

]
