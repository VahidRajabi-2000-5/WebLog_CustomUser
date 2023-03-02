from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Post
from .forms import PostForm


# def posts_list_view(request):
#     post = Post.objects.filter(status="Pub").order_by('-datetime_modified',)
#     return render(request, 'blog/posts_list.html', {'post': post})

class postsListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(status="Pub").order_by('-datetime_modified',)


# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = "post"


# def post_create_view(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:  # GET
#         form = PostForm()
#     return render(request, 'blog/post_create.html', {'form': form})

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('post_detail', args=[post.pk]))
#     return render(request, 'blog/post_create.html', {'form': form})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', {'post': post})

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts_list')

    # def get_success_url(self):
    #     return reverse('posts_list')
    