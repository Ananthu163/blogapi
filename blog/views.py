from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from blog.serializers import UserSerializers,PostSerializer
from rest_framework import authentication,permissions
from blog.models import Post


class UserCreateView(CreateAPIView):

    serializer_class=UserSerializers


class PostListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    def perform_create(self,serializers):

        return serializers.save(owner=self.request.user)


class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]
    