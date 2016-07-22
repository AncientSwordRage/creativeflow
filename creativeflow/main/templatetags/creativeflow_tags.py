from django import template  # NOQA
from django.core.urlresolvers import reverse, NoReverseMatch
import re
register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    """Add the active class to the element."""
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''
