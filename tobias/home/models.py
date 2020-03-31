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
    TitleBlock,
    SectionHeaderBlock,
    FeaturedSectionBlock,
    CodeBlock,
    PlotBlock,
    ImageBlock,
    LinkBlock,
    InternalLinkBlock,
    ButtonBlock,
)


class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"

    intro = RichTextField(blank=True)

    content = StreamField(
        [
            ("richtext", blocks.RichTextBlock()),
            ("title_block", TitleBlock()),
            ("section_header", SectionHeaderBlock()),
            ("featured_section", FeaturedSectionBlock()),
            ("image_block", ImageBlock()),
            ("linkblock", LinkBlock()),
            ("internallinkblock", InternalLinkBlock()),
            ("button", ButtonBlock()),
            ("plot", PlotBlock()),
            ("code", CodeBlock()),
            ("embed", EmbedBlock()),
            ("html", blocks.RawHTMLBlock()),
            ("image", ImageChooserBlock()),
        ],
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        StreamFieldPanel("content"),
    ]


class FyiPage(HomePage):
    """Basically the about page."""

    template = "home/fyi_page.html"
