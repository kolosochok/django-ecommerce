from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [

	# Blogpage
	path('', views.blog_view, name='blog'),

	# Post Details
	path('post/<pid>/', views.blog_detail_view, name='blog-detail'),

	# Blog Category
	path('category/<cid>/', views.blog_category_view, name="blog-category"),

	# Blog Tags
	path('tag/<slug:tag_slug>/', views.blog_tags, name='blog-tag'),

	# Add Post Comment
	path('ajax-add-comment/<int:pid>/', views.ajax_add_comment, name='ajax-add-comment'),

]