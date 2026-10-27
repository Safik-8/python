from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm


# ─────────────────────────────────────────────
# LIST  –  GET /blog/
# ─────────────────────────────────────────────
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


# ─────────────────────────────────────────────
# DETAIL  –  GET /blog/<pk>/
# ─────────────────────────────────────────────
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# ─────────────────────────────────────────────
# CREATE  –  GET/POST /blog/new/
# ─────────────────────────────────────────────
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['action'] = 'Create'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, f'✅ Post "{form.instance.title}" created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '❌ Please fix the errors below.')
        return super().form_invalid(form)


# ─────────────────────────────────────────────
# UPDATE  –  GET/POST /blog/<pk>/edit/
# ─────────────────────────────────────────────
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['action'] = 'Edit'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, f'✅ Post "{form.instance.title}" updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '❌ Please fix the errors below.')
        return super().form_invalid(form)


# ─────────────────────────────────────────────
# DELETE  –  GET/POST /blog/<pk>/delete/
# ─────────────────────────────────────────────
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        messages.success(self.request, f'🗑️ Post "{self.object.title}" deleted.')
        return super().form_valid(form)
