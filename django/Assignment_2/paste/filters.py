from .models import Post
import django_filters
from django.utils import timezone

class PostFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr='icontains')
	content = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Post
		fields = ['title', 'content']

	@property
	def qs(self):
		parent = super(PostFilter, self).qs

		return parent.filter(is_disabled=False).exclude(expiry_date__lte=timezone.now()).order_by('-date_posted')
