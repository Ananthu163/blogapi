from django.shortcuts import render,get_object_or_404
# Create your views here.
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from blog.serializers import UserSerializers,PostSerializer,CommentSerializer
from rest_framework import authentication,permissions
from blog.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response


class UserCreateView(CreateAPIView):

    serializer_class=UserSerializers


class PostListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    def perform_create(self,serializers):

        return serializers.save(owner=self.request.user)


class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]
    


class CommentCreateView(CreateAPIView):

    serializer_class=CommentSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self,serializers):

        id=self.kwargs.get("pk")

        post_instance=get_object_or_404(Post,id=id)

        serializers.save(post_object=post_instance,owner=self.request.user)
        

class PostLikedView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        post_object=get_object_or_404(Post,id=id)

        if request.user in post_object.liked_by.all():

            post_object.liked_by.remove(request.user) #removing from many to many field

            return Response(data={"message":"unliked"})

        else:
        
            post_object.liked_by.add(request.user) #adding to many to many field

            return Response(data={"message":"liked"})

