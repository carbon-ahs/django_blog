from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
