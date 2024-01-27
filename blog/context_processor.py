import random
from blog.models import Category
from taggit.models import Tag

def blog_context(request):

	blog_categories = Category.objects.all()

	all_blog_tags = Tag.objects.filter(post__isnull=False).distinct()
	random_blog_tags = random.sample(list(all_blog_tags), min(6, len(all_blog_tags)))

	return {
		'blog_categories': blog_categories,
		'random_blog_tags': random_blog_tags
	}