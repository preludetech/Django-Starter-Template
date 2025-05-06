from django.template import loader
import tempfile
from pathlib import Path
import markdown
from django.utils.safestring import mark_safe
from django.conf import settings
import nh3


def render_markdown(markdown_text, request, context=None):
    context = context or {}

    markdown_text = nh3.clean(markdown_text, tags=settings.MARKDOWN_ALLOWED_TAGS)

    if settings.MARKDOWN_TEMPLATE_RENDER_ON:

        temp = tempfile.NamedTemporaryFile(
            prefix="template_",
        )

        temp.write(str.encode(markdown_text))
        temp.seek(0)
        content = loader.render_to_string(
            Path(temp.name).stem, context=context, request=request, using=None
        )
    else:
        content = markdown_text

    md = markdown.Markdown(extensions=["fenced_code", "mdx_headdown"])
    return mark_safe(md.convert(content))
