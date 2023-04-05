from rest_framework import serializers
from posts.models import Comment, Post, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'text', 'pub_date', 'id', 'image', 'group')
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'id')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('author', 'text', 'created', 'id', 'post')
        read_only_fields = ('post', 'author',)
