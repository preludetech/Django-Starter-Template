from django.template import loader
import tempfile
from pathlib import Path
import markdown
from django.utils.safestring import mark_safe

# from django.template import engines


def render_markdown(markdown_text, request, context=None):
    context = context or {}

    temp = tempfile.NamedTemporaryFile(
        prefix="template_",
    )

    temp.write(str.encode(markdown_text))
    temp.seek(0)
    content = loader.render_to_string(
        Path(temp.name).stem, context=context, request=request, using=None
    )
    md = markdown.Markdown(extensions=["fenced_code", "mdx_headdown"])
    return mark_safe(md.convert(content))


# def render_markdown(markdown_text, request, context=None):
#     django_engine = engines["django"]
#     template = django_engine.from_string(markdown_text)
#     # content = template.render_to_string(
#     #     context=context,
#     #     request=request,
#     # )

#     content = template.render(context, request)

#     md = markdown.Markdown(extensions=["fenced_code", "mdx_headdown"])
#     return mark_safe(md.convert(content))
