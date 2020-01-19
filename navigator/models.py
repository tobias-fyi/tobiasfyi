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

    @property
    def link(self) -> str:
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return "#"

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing Title"


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

