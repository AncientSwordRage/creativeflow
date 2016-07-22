"""Creativeflow URL Configuration the blog app."""
from django.conf.urls import url
from django.views.generic.dates import (ArchiveIndexView,
                                        YearArchiveView,
                                        MonthArchiveView)
from .models import Post
from .views import BlogDetailView
urlpatterns = [
    url(r'^posts\/(?P<year>\d{4})\/(?P<month>\d{2})\/(?P<day>\d{2})\/(?P<pk>\d+)',
        BlogDetailView.as_view(), name="blog-detail"),
    url(r'^(?:posts)?/?$',
        ArchiveIndexView.as_view(model=Post,
                                 date_field="published",
                                 date_list_period='month',
                                 template_name="post_archive"),
        name="blog-archive-list"),
    url(r'posts/(?P<year>\d{4})/?$',
        YearArchiveView.as_view(model=Post,
                                date_field="published",
                                template_name="post_archive_year"),
        name="post_year_archive"),
    url(r'posts/(?P<year>\d{4})/(?P<month>\d{2})/?$',
        MonthArchiveView.as_view(model=Post,
                                 date_field="published",
                                 month_format='%m',
                                 template_name="post_archive_month"),
        name="post_month_archive"),
]
