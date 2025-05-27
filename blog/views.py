from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required



def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views_count += 1
    post.save(update_fields=["views_count"])
    return render(request, "blog/post_detail.html", {"post": post})


@login_required(login_url='login')
def post_create(request):
    login_url = 'login'
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Пост успешно создан.")
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


@login_required(login_url='login')
def post_update(request, pk):
    login_url = 'login'
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Пост успешно обновлён.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form})


@login_required(login_url='login')
def post_delete(request, pk):
    login_url = 'login'
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Пост удалён.")
        return redirect("post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})
