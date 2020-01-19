"""
Navigator :: Models for navigation system
"""

from django.db import models

from django_extensions.db.fields import AutoSlugField

from wagtail.snippets.models import register_snippet
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    FieldPanel,
    InlinePanel,
    PageChooserPanel,
)


class NavItem(Orderable):
    """Individual navigation link."""

    link_title = models.CharField(max_length=100, null=True, blank=True,)
    link_url = models.CharField(max_length=500, blank=True,)
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    # Links Orderable to ClusterableModel
    page = ParentalKey("Nav", related_name="nav_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    # TODO: add properties
    # link
    # title


@register_snippet
class Nav(ClusterableModel):
    """Main navigation menu."""

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)

    panels = [
        MultiFieldPanel(
            [FieldPanel("title"), FieldPanel("slug"),], heading="Navigation"
        ),
        InlinePanel("nav_items", label="Nav Item"),
    ]

    def __str__(self):
        return self.title

