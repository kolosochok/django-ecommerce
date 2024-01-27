from django.contrib import admin
from blog.models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'blog_image', 'pid']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'cid']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['user', 'post']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)