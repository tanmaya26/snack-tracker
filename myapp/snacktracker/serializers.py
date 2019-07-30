from rest_framework import serializers
from .models import Snack, Request, Image, Like, Tag, Dislike, User


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ('id', 'snack_name', 'snack_quantity', 'snack_description', 'snack_image', 'snack_tag')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'user', 'snack', 'quantity', 'description', 'tag', 'image')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'snack')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'snack', 'likes')


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ('user', 'snack', 'dislikes')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'password', 'email')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'snack', 'name')
