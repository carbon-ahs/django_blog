from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    queryset = Post.objects.order_by("-created_at")
    context_object_name = "post_list"
    template_name = "home.html"

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Home"
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        title = Post.objects.get(pk=pk).title
        context["page_title"] = title
        return context


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        title = "New Post"
        context["page_title"] = title
        return context


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        title = "Edit Post"
        context["page_title"] = title
        return context


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        title = "Delete Post"
        context["page_title"] = title
        return context
