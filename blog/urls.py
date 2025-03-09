from django.urls import path
from blog import views
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns=[

    path("users/",views.UserCreateView.as_view()),
    path("posts/",views.PostListCreateView.as_view()),
    path("posts/<int:pk>/",views.PostRetrieveUpdateDestroyView.as_view()),
    path("posts/<int:pk>/comments/",views.CommentCreateView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("posts/<int:pk>/like/",views.PostLikedView.as_view()),
]