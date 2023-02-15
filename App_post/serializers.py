from rest_framework import serializers
from .models import Task, Post, Like, Comment
from Auth.models import CustomUser
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'get_full_name']


class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ['id','caption','image','created', 'updated','like_count']
 
    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        return Post.objects.create(author=author, **validated_data)


class PostSerializerPost(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ['id','caption','image','created', 'updated']
 
    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        return Post.objects.create(author=author, **validated_data)


class PostSerializerGet(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['author', 'id','image', 'caption', 'created', 'updated','like_count']


class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id',)


class LikeListSerializer(serializers.ModelSerializer):
    liked_by = AuthorSerializer(read_only=True)
    class Meta:
        model =Post
        fields = ['liked_by',]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['body','image']

    def create(self, validated_data):
        request = self.context.get('request')
        kwargs_from_view = request.parser_context.get('view').kwargs
        validated_data['commented_by'] = request.user
        validated_data['post'] = Post.objects.filter(id=kwargs_from_view.get('post_id')).first()
        instance = self.Meta.model.objects.create(**validated_data)
        instance.save()
        return instance

    

class CommentSerializerGet(serializers.ModelSerializer):
    commented_by = AuthorSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','commented_by','body','image')


class CommentSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['body','image']

    def create(self, validated_data):
        request = self.context.get('request')
        kwargs_from_view = request.parser_context.get('view').kwargs
        validated_data['commented_by'] = request.user
        validated_data['post'] = Post.objects.filter(id=kwargs_from_view.get('post_id')).first()
        instance = self.Meta.model.objects.create(**validated_data)
        instance.save()
        return instance

    



#######Task Serializer######


class TaskSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id','title','author', 'description', 'complete']
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return Task.objects.create(**validated_data)


