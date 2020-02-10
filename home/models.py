from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from utils.blocks import (
    CodeBlock,
    CardBlock,
    PlotBlock,
    LinkBlock,
    InternalLinkBlock,
    ContactBlock,
)


class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    intro = RichTextField(blank=True)
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content = StreamField(
        [
            ("richtext", blocks.RichTextBlock()),
            ("linkblock", LinkBlock()),
            ("internallinkblock", InternalLinkBlock()),
            ("featured", blocks.PageChooserBlock()),
            ("html", blocks.RawHTMLBlock()),
            ("cards", CardBlock()),
            ("image", ImageChooserBlock()),
            ("embed", EmbedBlock()),
            ("code", CodeBlock()),
            ("contact", ContactBlock()),
        ],
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        ImageChooserPanel("header_image"),
        StreamFieldPanel("content"),
    ]


class FyiPage(HomePage):
    """Basically the about page."""

    template = "home/fyi_page.html"


class ElementPage(Page):
    """Render Stellar elements."""

    template = "home/elements.html"
