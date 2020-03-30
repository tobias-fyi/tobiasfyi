"""
Workshop \\ models :: Project portfolio
"""

from django import forms
from django.db import models

from modelcluster.fields import ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.core.models import Page, Orderable
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
from wagtail.search import index

from blog.models import BlogPageTag
from utils.blocks import (
    CodeBlock,
    PlotBlock,
    ImageBlock,
    LinkBlock,
    InternalLinkBlock,
)


class ProjectIndexPage(Page):
    """Page model for index page listing all projects."""

    template = "workshop/project_index_page.html"

    intro = RichTextField(blank=True)
    content = StreamField(
        [
            ("richtext", blocks.RichTextBlock()),
            ("image_block", ImageBlock()),
            ("code_block", CodeBlock()),
            ("link_block", LinkBlock()),
            ("internal_link_block", InternalLinkBlock()),
            ("plot", PlotBlock()),
            ("embed", EmbedBlock()),
            ("html", blocks.RawHTMLBlock()),
            ("image", ImageChooserBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        StreamFieldPanel("content"),
    ]


class ProjectPage(Page):
    """Page model for individual projects."""

    template = "workshop/project_page.html"

    intro = RichTextField(max_length=300)
    date_begin = models.DateField("Project start date")
    date_end = models.DateField("Project end date", blank=True)
    header_image = models.ForeignKey(
        "wagtailimages.Image", null=True, on_delete=models.SET_NULL, related_name="+",
    )
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)
    repo = models.URLField(blank=True)
    content = StreamField(
        [
            ("richtext", blocks.RichTextBlock()),
            ("image_block", ImageBlock()),
            ("code_block", CodeBlock()),
            ("linkblock", LinkBlock()),
            ("internal_link_block", InternalLinkBlock()),
            ("plot", PlotBlock()),
            ("blockquote", blocks.BlockQuoteBlock()),
            ("embed", EmbedBlock()),
            ("html", blocks.RawHTMLBlock()),
            ("image", ImageChooserBlock()),
        ]
    )

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("content"),
        index.FilterField("date_begin"),
        index.FilterField("date_end"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("date_begin"),
                FieldPanel("date_end"),
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
                FieldPanel("tags"),
            ],
            heading="Project Metadata",
        ),
        ImageChooserPanel("header_image"),
        FieldPanel("intro"),
        StreamFieldPanel("content"),
    ]
