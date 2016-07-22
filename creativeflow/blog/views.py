from django.views.generic import DetailView  # NOQA

from .models import Post
# Create your views here.


class BlogDetailView(DetailView):
    """CBV for blog post detail."""

    model = Post
    template_name = "blog_detail.html"
    context_object_name = "blog_object"
