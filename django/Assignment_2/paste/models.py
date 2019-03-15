from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_cryptography.fields import encrypt


class Post(models.Model):
	title = encrypt(models.CharField(max_length=100))
	content = encrypt(models.TextField())
	date_posted = models.DateTimeField(default=timezone.now) #auto_now=True to update date to last modified
	user = encrypt(models.ForeignKey(User, on_delete=models.CASCADE))
	is_disabled = models.BooleanField(default=False)
	expiry_date = models.DateTimeField(null=True, blank=True)
	private = models.BooleanField(default=False)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
