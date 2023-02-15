from .models import Task, Post, Like, Comment
from rest_framework import generics,parsers
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
        TaskSerializer, PostSerializer,
        CommentSerializer, PostSerializerPost, 
        PostSerializerGet, LikeSerializer,
        LikeListSerializer, CommentSerializerGet,
        CommentSerializerPost
    )


class PostList(generics.ListAPIView):
    search_fields = ['caption']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PostSerializerGet
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
            post = Post.objects.all()
            return post

class CreatePost(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializerPost
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    lookup_field = 'id'

class PostUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    lookup_field = 'id'

    
class PostDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    lookup_field = 'id'

class LikeApi(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    def get_object(self, pk):
        like = Post.objects.get(pk = pk)
        return like
        
    def post(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        likers = post.likes.all().values_list('liked_by', flat = True)
        if request.user.id in likers:
            post.like_count -= 1
            post.likes.filter(liked_by = request.user).delete()
        else:
            post.like_count += 1
            like = Like(liked_by = request.user, post = post)
            like.save()
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data, status = status.HTTP_200_OK)

     
class LikedUserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeListSerializer
    
    def get_queryset(self):
        likes = Like.objects.filter(post = self.kwargs.get('pk'))
        return likes

class Create_comment(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class update_comment(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerPost

class delete_comment(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializerGet
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
            comment = Comment.objects.filter(post = self.kwargs.get('pk'))
            return comment

    
####### TaskView ####


class TaskList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    search_fields = ['^title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        task = Task.objects.filter(author=self.request.user)
        return task

class TaskCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
     
class TaskDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 
    lookup_field = 'id'

class TaskUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 
    lookup_field = 'id'

class TaskDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 
    lookup_field = 'id'