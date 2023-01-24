from django.urls import path
from users.views import user_views

urlpatterns = [
    path("", user_views.UserListCreateView.as_view()),
]
