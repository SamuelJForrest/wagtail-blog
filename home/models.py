from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from streams import blocks


class HomePage(Page):
    ''' Homepage model '''

    template = 'home/home_page.html'
    max_count = 1

    subpage_types = [
        'blog.BlogListingPage',
    ]

    banner_title = models.CharField(
        max_length=100,
        null=True,
        blank=False,
    )

    banner_text = RichTextField()

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner_link = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
    )

    banner_link_text = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )

    content = StreamField(
        [
            ("icon_grid", blocks.IconGridBlock()),
            ("rich_text", blocks.RichTextBlock()),
        ],
        use_json_field=True,
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_text"),
            FieldPanel("banner_image"),
            PageChooserPanel("banner_cta"),
            MultiFieldPanel([
                FieldPanel("banner_link_text"),
                FieldPanel("banner_link")
            ], heading="External Link")
        ], heading="Banner"),
        FieldPanel('content')
    ]

    class Meta:
        ''' Home page meta settings '''
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
