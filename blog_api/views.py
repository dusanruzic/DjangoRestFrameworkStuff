from django.shortcuts import render
from blog.models import Post
from rest_framework import generics
from blog_api.serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, BasePermission

from datetime import datetime, timedelta

class CustomPostDetailPermission(BasePermission):
    message = None
    def has_object_permission(self, request, view, obj):
        #if we want to update message on every request, you should pass the value to message here in method, rather than above.
        self.message = f"You do not have permission to access other's post details. Access is forbiden by {datetime.now() + timedelta(minutes=60)}"
        return obj.author == request.user


#endpoint to list all items or create new item
class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

#retrieve concrete object or delete them (pk required)
class PostDetail(generics.RetrieveDestroyAPIView, CustomPostDetailPermission):
    permission_classes = [CustomPostDetailPermission,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer