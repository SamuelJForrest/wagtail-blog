from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from streams import blocks


class BlogListingPage(Page):
    '''Blog listing page'''

    template = 'blog/blog_listing.html'

    subpage_types = [
        'blog.BlogDetailPage',
    ]

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Overwrites default title"
    )

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        FieldPanel('banner_image'),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        return context


class BlogDetailPage(Page):
    '''Individual blog pages'''

    custom_title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Overwrites default title"
    )

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )

    content = StreamField(
        [
            ("icon_grid", blocks.IconGridBlock())
        ],
        use_json_field=True,
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("banner_image"),
        FieldPanel("content"),
    ]
