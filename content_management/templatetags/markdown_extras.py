import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from lxml import etree
import re


def img(src):
    return f'<img src="{src}" />'


def youtube(src):
    return todo


def flip(flip):
    return todo


functions = {
    "img": img,
    "flip": flip,
    "youtube": youtube,
}


# import re


# def parse_key_value_string(s):

#     print("=============================")
#     print(s)
#     print("=============================")

#     pattern = r"(\w+)\s*=\s*(?:'([^']*)'|(\d+))"
#     matches = re.findall(pattern, s)
#     result = {}
#     for key, str_value, num_value in matches:
#         if str_value:
#             result[key] = str_value
#         elif num_value:
#             result[key] = int(num_value)

#     return result


class CustomBlocks(BlockProcessor):

    RE_PATTERN = "{%(.*)%}"

    def test(self, parent, block):
        if re.search(self.RE_PATTERN, block):
            return True

    def run(self, parent, blocks):
        initial = blocks[0]
        inner = re.search(self.RE_PATTERN, initial).groups()[0]
        parts = inner.split()
        function_name = parts[0]
        args = parts[1:]
        # kwargs = parse_key_value_string(" ".join(parts[1:]))
        # print(kwargs)
        blocks[0] = functions[function_name](*args)
        return True


class CustomTagExtension(Extension):
    def extendMarkdown(self, md) -> None:
        """
        Add the various processors and patterns to the Markdown Instance.

        This method must be overridden by every extension.

        Arguments:
            md: The Markdown instance.

        """
        # md.registerExtension(self)
        md.parser.blockprocessors.register(
            CustomBlocks(md.parser), "custom", priority=175
        )


register = template.Library()


@register.filter
@stringfilter
def render_md(value):
    md = markdown.Markdown(
        extensions=["fenced_code", "mdx_headdown", CustomTagExtension()]
    )
    return mark_safe(md.convert(value))
