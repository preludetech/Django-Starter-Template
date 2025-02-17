import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def render_md(value):
    md = markdown.Markdown(extensions=["fenced_code", "mdx_headdown"])
    return mark_safe(md.convert(value))
