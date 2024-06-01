from rest_framework import serializers

from .models import Blog,Catagory,Comment,Like,PostView

class BlogSerializer(serializers.ModelSerializer):
    
    toplam_yorum = serializers.SerializerMethodField()
    toplam_like = serializers.SerializerMethodField()
    toplam_goruntulenme = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['id','toplam_yorum','toplam_like','toplam_goruntulenme']

    def create(self, validated_data):
        user = self.context['request'].user
        main_user = Blog.objects.create(user=user, **validated_data)
        return main_user

    def get_toplam_yorum(self, obj):
        return obj.comment.count()
    
    def get_toplam_like(self,obj):
        return obj.like.count()      
     
    def get_toplam_goruntulenme(self, obj):
        return PostView.objects.filter(blog=obj, post_views=True).count()
    

class UserBlogSerializer(serializers.ModelSerializer):
    view_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        exclude = ['status']

    def get_view_count(self, obj):
        return PostView.objects.filter(blog=obj, post_views=True).count()


class CatagorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Catagory
        fields = '__all__'
        read_only_fields = ['id']

        
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id']



class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['id']



class PostViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostView
        fields = '__all__'
        read_only_fields = ['id']


