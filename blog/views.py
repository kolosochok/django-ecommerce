from django.shortcuts import render
from django.http import JsonResponse
from blog.models import Post, Comment, Category
from blog.forms import CommentFrom
from taggit.models import Tag

def blog_view(request):
	posts = Post.objects.filter(post_status='published').order_by("-date_created")

	context = {
		"posts": posts,
	}
	return render(request, 'blog/blog.html', context)

def blog_category_view(request, cid):
	category = Category.objects.get(cid=cid)
	posts = Post.objects.filter(
		post_status='published', categories=category
	).order_by("-date_created")

	context = {
		"category": category,
		"posts": posts,
	}
	return render(request, "blog/category.html", context)

def blog_detail_view(request, pid):
	post = Post.objects.get(pid=pid)
	posts = Post.objects.filter(categories__in=post.categories.all()).exclude(pid=pid).distinct()
	comments = Comment.objects.filter(post=post).order_by('-date_created')

	comment_form = CommentFrom()

	make_comment = True
	if request.user.is_authenticated:
		user_comment_count = Comment.objects.filter(
			user=request.user, 
			post=post
		).count() 

		if user_comment_count > 0:
			make_comment = False

	context = {
		"post": post,
		"comments": comments,
		"comment_form": comment_form,
		"make_comment": make_comment,
		"posts": posts,
	}
	return render(request, 'blog/blog-detail.html', context)

def blog_tags(request, tag_slug=None):
	posts = Post.objects.filter(post_status='published').order_by('-id')

	tag = None
	if tag_slug:
		tag = Tag.objects.get(slug=tag_slug)
		posts = posts.filter(tags__in=[tag])

	context = {
		'posts': posts,
		'tag': tag,
	}
	return render(request, 'blog/tag.html', context)

def ajax_add_comment(request, pid):
	post = Post.objects.get(pk=pid)
	user = request.user
	image = user.image.url

	comment = Comment.objects.create(
		user=user,
		post=post,
		body=request.POST['comment'],
	)
	
	context = {
		'user': user.username,
		'comment': request.POST['comment'],
		'image': image
	}
	return JsonResponse(
		{
			'bool': True,
			'context': context,
		}
	)