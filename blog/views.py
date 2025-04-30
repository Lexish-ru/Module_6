from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by('-created_at')


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')
