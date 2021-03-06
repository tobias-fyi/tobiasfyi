"""StreamFields Blocks."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.StructBlock):
    """Block for styling headers similar to page-title component."""

    title = blocks.CharBlock(required=True, help_text="Title content")
    permalink = blocks.CharBlock(required=False, help_text="HTML class for permalink")

    class Meta:
        template = "utils/title_block.html"
        icon = "bold"
        label = "Title"


class SectionHeaderBlock(blocks.StructBlock):
    """Block for styling headers similar to page-title component."""

    header = blocks.CharBlock(required=True, help_text="Header content")
    permalink = blocks.CharBlock(required=False, help_text="HTML class for permalink")

    class Meta:
        template = "utils/section_header_block.html"
        icon = "link"
        label = "Section Header"


class FeaturedSectionBlock(blocks.StructBlock):
    """Block for displaying a list of featured content from a page's children."""

    header = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Title to display above the featured section",
    )
    permalink = blocks.CharBlock(required=False, help_text="HTML class for permalink")
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
    featured_section = blocks.PageChooserBlock(
        required=False,
        help_text="First featured section for the homepage. Will display up to "
        "three child items.",
    )

    class Meta:
        template = "utils/featured_section_block.html"
        icon = "link"
        label = "Featured Section"


class CodeBlock(blocks.StructBlock):
    """Block of text to be rendered and highlighted as code."""

    language = blocks.CharBlock(required=False)
    caption = blocks.RichTextBlock(required=False)
    code = blocks.TextBlock(required=True)

    class Meta:
        template = "utils/code_block.html"
        icon = "code"
        label = "Code Block"


class PlotBlock(blocks.StructBlock):
    """Base class for interactive plots."""

    caption = blocks.CharBlock(max_length=240, required=False)
    description = blocks.RichTextBlock(required=False)
    # TODO: research best practices for integrating Plotly
    plot = blocks.RawHTMLBlock(required=True, help_text="HTML to generate plot.")

    class Meta:
        template = "utils/plot_block.html"
        icon = "placeholder"
        label = "Plot"


class ImageBlock(blocks.StructBlock):
    """Base class for images and static plots."""

    caption = blocks.CharBlock(max_length=240, required=True)
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

    description = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "utils/internal_link_block.html"
        label = "Internal Link"


class ButtonBlock(LinkBlock):
    """Block containing a simple button that leads to internal or external page."""

    class Meta:
        template = "utils/button_block.html"
        label = "Button"
