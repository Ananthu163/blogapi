from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post

class UserSerializers(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["id","username","email","password"]

        read_only_fields=["id"]

    def create(self,validated_data):

        return User.objects.create_user(**validated_data)

class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model=Post

        fields="__all__"

        read_only_fields=["id","created_at","owner"]