from django.shortcuts import render  # NOQA
from blogs import Blogs
# Create your views here.


def home(request, template='path/to/template'):
    """Prepare content for main page."""
    context = {
        'blogs': Blogs.objects.all(),
    }
    return (request, template, context)
