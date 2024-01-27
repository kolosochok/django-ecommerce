from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe

class User(AbstractUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=100)
	name = models.CharField(max_length=100, null=True, blank=True, default='')
	phone = models.CharField(max_length=100, null=True, blank=True, default='')
	bio = models.CharField(max_length=100, null=True, blank=True, default='')
	image = models.ImageField(upload_to='account-images', default="user.jpg")

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['username']

	def user_image(self):
		return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

	def __str__(self):
		return self.username
