from django.urls import path,include

from rest_framework import routers

from .views import BlogMVS,CatagoryMVS,CommentMVS,LikeMVS,PostViewMVS

router = routers.DefaultRouter()
router.register('blog',BlogMVS)
router.register('catagory',CatagoryMVS)
router.register('comment',CommentMVS)
router.register('like',LikeMVS)
router.register('post',PostViewMVS)


urlpatterns = [
       path('',include(router.urls))
]


