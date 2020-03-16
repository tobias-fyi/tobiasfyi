"""StreamFields Blocks."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CodeBlock(blocks.StructBlock):
    """Block of text to be rendered and highlighted as code."""

    title = blocks.CharBlock(required=True, help_text="Name of code block.")
    code = blocks.TextBlock(required=True, help_text="Text to be rendered as code.")
    language = blocks.CharBlock(required=True, help_text="Programming language.")
    caption = blocks.RichTextBlock(
        required=False, help_text="Brief description of code snippet."
    )

    class Meta:
        template = "utils/code_block.html"
        icon = "code"
        label = "Code Block"


class PlotBlock(blocks.StructBlock):
    """Base class for interactive plots."""

    title = blocks.CharBlock(max_length=42, required=True, help_text="Short title.")
    caption = blocks.CharBlock(
        max_length=240, required=True, help_text="Short summary."
    )
    description = blocks.RichTextBlock(required=False, help_text="Long description.")
    # TODO: research best practices for integrating Plotly
    plot = blocks.RawHTMLBlock(required=True, help_text="HTML code to generate plot.")

    class Meta:
        template = "utils/plot_block.html"
        icon = "placeholder"
        label = "Plot"


class ImageBlock(blocks.StructBlock):
    """Base class for images and static plots."""

    title = blocks.CharBlock(max_length=42, required=True, help_text="Short title.")
    caption = blocks.CharBlock(
        max_length=240, required=True, help_text="Short summary."
    )
    description = blocks.RichTextBlock(required=False, help_text="Long description.")
    image = ImageChooserBlock()

    class Meta:
        template = "utils/image_block.html"
        icon = "image"
        label = "Image block"


class LinkStructValue(blocks.StructValue):
    """Custom logic for links."""

    def url(self):
        link_page = self.get("link_page")
        link_url = self.get("link_url")

        if link_page:
            return link_page.url
        elif link_url:
            return link_url

        return None


class LinkBlock(blocks.StructBlock):
    """Base class for formatting featured links to external or internal pages."""

    title = blocks.CharBlock(required=True)
    link_page = blocks.PageChooserBlock(required=False)
    link_url = blocks.URLBlock(required=False)

    class Meta:
        template = "utils/link_block.html"
        icon = "link"
        label = "In-line Featured Link"
        value_class = LinkStructValue


class InternalLinkBlock(LinkBlock):
    """Block for internal links, formatted like an item on an index page."""

    description = blocks.RichTextBlock(required=True)
    image = ImageChooserBlock()

    class Meta:
        template = "utils/internal_link_block.html"
        label = "Internal Link"

