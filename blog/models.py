"""
blog \\ models :: non-fiction or technical pieces
"""

from django import forms
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

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

from utils.blocks import (
    CodeBlock,
    CardBlock,
    PlotBlock,
    LinkBlock,
    ElementBlock,
)


class BlogIndexPage(Page):
    """Index of all individual blog pages."""

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
            ("richtext_section", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("embed", EmbedBlock()),
            ("html", blocks.RawHTMLBlock()),
            ("featured_content", blocks.PageChooserBlock()),
            ("linkblock", LinkBlock()),
            ("cards", CardBlock()),
        ],
        null=True,
        blank=True,
    )

    def get_context(self, request):
        """Add custom content and/or config to the context.
        Order the child pages by reverse published date"""

        # Include only published posts, ordered in reverse chron
        context = super().get_context(request)
        # Get all blog posts
        posts = self.get_children().live().public().order_by("-first_published_at")

        # Paginate all blog posts into 4 per page
        paginator = Paginator(posts, 4)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and ?page=x is an integer
            blog = paginator.page(page)
        except PageNotAnInteger:
            # If ?page=x is not an integer, return the first page
            blog = paginator.page(1)
        except EmptyPage:
            # If ?page=x is out of range, return the last page
            blog = paginator.page(paginator.num_pages)

        context["blog"] = blog
        return context

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        ImageChooserPanel("header_image"),
        StreamFieldPanel("content"),
    ]


# === Tags and Categories Configuration === #


class BlogPageTag(TaggedItemBase):
    """List of pages associated with a single tag."""

    content_object = ParentalKey(
        "BlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class BlogTagIndexPage(Page):
    """Index page for blog tags."""

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get("tag")
        blog = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context["blog"] = blog
        return context


@register_snippet
class BlogCategory(models.Model):
    """Broad classification of blog posts."""

    name = models.CharField(max_length=240)
    icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [FieldPanel("name"), ImageChooserPanel("icon")]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"


# === Individual Blog Pages === #


class BlogPage(Page):
    """Configuration of individual blog post pages."""

    date = models.DateField("Post date")
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    intro = models.CharField(max_length=250)
    body = StreamField(
        [
            ("richtext_section", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("code_block", CodeBlock()),
            ("embed", EmbedBlock()),
            ("html", blocks.RawHTMLBlock()),
            ("related_content", blocks.PageChooserBlock()),
            ("link", LinkBlock()),
            ("cards", CardBlock()),
            ("elements", ElementBlock()),  # TODO: make into static template
        ],
        null=True,
        blank=True,
    )
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
        index.FilterField("date"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
                FieldPanel("tags"),
            ],
            heading="Post Metadata",
        ),
        ImageChooserPanel("header_image"),
        FieldPanel("intro"),
        StreamFieldPanel("body"),
        InlinePanel("related_content", label="Related content"),
    ]

    promote_panels = [ImageChooserPanel("feed_image")]


class BlogPageRelatedContent(Orderable):
    """Configure the related content panel on blog edit page."""

    page = ParentalKey(
        BlogPage, on_delete=models.CASCADE, related_name="related_content"
    )
    name = models.CharField(max_length=255)
    content = StreamField(
        [
            ("link", blocks.URLBlock()),
            ("linkblock", LinkBlock()),
            ("related_content", blocks.PageChooserBlock()),
            ("richtext_section", blocks.RichTextBlock()),
            ("cards", CardBlock()),
            ("image", ImageChooserBlock()),
            ("code_block", CodeBlock()),
            ("embed", EmbedBlock()),
            ("html", blocks.RawHTMLBlock()),
        ],
        null=True,
        blank=True,
    )

    panels = [FieldPanel("name"), StreamFieldPanel("content")]
