from django.shortcuts import render, get_object_or_404
from django.views.generic import (
	ListView, DetailView, 
	CreateView, UpdateView, DeleteView)
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'paste/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'paste/home.html'
	context_object_name = 'posts'
	paginate_by = 10

	def get_queryset(self):
		return Post.objects.filter(is_disabled=False).order_by('-date_posted')



class UserPostListView(ListView):
	model = Post
	template_name = 'paste/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(user=user).filter(is_disabled=False).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		return False

def about(request):
	return render(request, 'paste/about.html', {'title':'About'})
