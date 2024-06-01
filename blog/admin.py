from django.contrib import admin

from .models import Blog,Catagory,Like,Comment,PostView

admin.site.register(Blog)
admin.site.register(Catagory)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(PostView)

