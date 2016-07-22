"""Template Tags."""
from itertools import groupby
from calendar import month_name as months
from django import template
from blog.models import Post, SOCIAL_MEDIA

register = template.Library()


@register.simple_tag
def transformed_dates():
    """Convert date objects to a dictionary of years and months."""
    grouped_dates = groupby(Post.objects.datetimes('published', 'month'),
                            lambda date: date.year)

    def get_months(dates):
        return [{'name': months[d.month],
                 'num':str(d.month).zfill(2)} for d in dates]

    return [{"year": year, 'months': get_months(dates)}
            for year, dates in grouped_dates]


@register.simple_tag
def social_media():
    """Social Media Links."""
    return SOCIAL_MEDIA


@register.filter
def last_date(dates):
    """Get Last date in list."""
    return sorted(dates)[-1]


@register.filter
def first_date(dates):
    """Get Last date in list."""
    return sorted(dates)[0]
