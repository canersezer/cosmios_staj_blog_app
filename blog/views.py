from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Blog,Catagory,Comment,Like,PostView
from .serializers import BlogSerializer,CatagorySerializer,CommentSerializer,LikeSerializer,PostViewSerializer,UserBlogSerializer
from .permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly, IsAdminOrReadOnly, IsOwnerOrStaffOrPublished

class BlogMVS(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return BlogSerializer
        return UserBlogSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwnerOrStaffOrPublished]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        user = request.user if request.user.is_authenticated else None
        if user:
            post_view, created = PostView.objects.get_or_create(blog=instance, user=user, post_views=False)
            post_view.post_views = True
            post_view.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class CategoryMVS(viewsets.ModelViewSet):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CommentMVS(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class LikeMVS(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class PostViewsMVS(viewsets.ModelViewSet):
    queryset = PostView.objects.all()
    serializer_class = PostViewSerializer
    permission_classes = [IsAuthenticated]

