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


class CardBlock(blocks.StructBlock):
    """Cards with an image, a blurb of text, and a button each."""

    title = blocks.CharBlock(required=True, help_text="Title for group of cards.")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=100)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False, help_text="Button page will be used first."
                    ),
                ),
            ]
        )
    )

    class Meta:
        template = "utils/card_block.html"
        icon = "placeholder"
        label = "Cards"


class PlotBlock(blocks.StructBlock):
    """Base class for interactive plots."""

    title = blocks.CharBlock(
        max_length=42, required=True, help_text="Short title for the plot."
    )
    caption = blocks.CharBlock(
        max_length=240, required=True, help_text="Short summary of the plot."
    )
    description = blocks.RichTextBlock(
        required=False, help_text="Long description of plot."
    )
    # TODO: research best practices for integrating Plotly
    plot = blocks.RawHTMLBlock(required=True, help_text="HTML code to generate plot.")

    class Meta:
        template = "utils/plot_block.html"
        icon = "placeholder"
        label = "Plot"


class RelatedContentBlock(blocks.StructBlock):
    """Block to format related content links."""

    pass

