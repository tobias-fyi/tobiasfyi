"""
workshop \\ models :: portfolio and resume
"""

from django import forms
from django.db import models

from modelcluster.fields import ParentalManyToManyField
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

from utils.blocks import CodeBlock, CardBlock, PlotBlock


class ProjectIndexPage(Page):
    """Page model for index page listing all projects."""

    template = "workshop/project_index_page.html"

    intro = RichTextField(blank=True)
    content = StreamField(
        [
            ("richtext", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("embed", EmbedBlock()),
            ("html", blocks.RawHTMLBlock()),
            ("featured_projects", blocks.PageChooserBlock()),
            ("cards", CardBlock()),
            ("plot", PlotBlock()),
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

    intro = RichTextField()
    header_image = models.ForeignKey(
        "wagtailimages.Image", null=True, on_delete=models.SET_NULL, related_name="+",
    )
    date_begin = models.DateField("Project start date")
    date_end = models.DateField("Project completion date", blank=True)
    # TODO: stack
    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)
    repo = models.URLField(blank=True)
    content = StreamField(
        [
            ("richtext", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("code_block", CodeBlock()),
            ("embed", EmbedBlock()),
            ("html", blocks.RawHTMLBlock()),
            ("related_content", blocks.PageChooserBlock()),
            ("cards", CardBlock()),
            ("plot", PlotBlock()),
        ]
    )

    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
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
            ],
            heading="Project Metadata",
        ),
        ImageChooserPanel("header_image"),
        FieldPanel("intro"),
        StreamFieldPanel("content"),
    ]

    promote_panels = [ImageChooserPanel("feed_image")]

