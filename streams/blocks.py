''' Housing from StreamFields '''

from wagtail import blocks
from wagtail.blocks import RawHTMLBlock


class IconGridBlock(blocks.StructBlock):
    '''Icon Grid block'''

    title = blocks.CharBlock(
        required=True,
        max_length=256,
    )

    intro_text = blocks.CharBlock(
        required=True,
        max_length=256
    )

    items = blocks.ListBlock(
        blocks.StructBlock(
            [
                (
                    'icon',
                    RawHTMLBlock(
                        help_text="Paste SVG code here (Make sure to remove strokes from SVG codes.)", # noqa
                    )
                ),
                (
                    'title',
                    blocks.CharBlock(required=True, max_length=256)
                ),
                (
                    'text',
                    blocks.CharBlock(required=True, max_length=1024)
                ),
            ],
            label_format="{title}",
        ),
        collapsed=True,
        max_num=6,
    )

    class Meta: # noqa
        template = 'streams/icon_grid_block.html'
        icon = "table"
        label = "Icon Grid Block"


class RichTextBlock(blocks.StructBlock):
    '''Rich text editor block'''

    content = blocks.RichTextBlock()

    class Meta: # noqa
        template = 'streams/richtext.html'
        icon = 'edit'
        label = 'Rich Text Block'


class HighLightsBlock(blocks.StructBlock):
    '''Highlights block'''

    title = blocks.CharBlock(
        max_length=256,
        null=True,
        blank=True
    )

    items = blocks.ListBlock(
        blocks.StructBlock(
            [
                (
                    'title',
                    blocks.CharBlock(
                        max_length=256,
                        blank=True
                    )
                ),
                (
                    'content',
                    blocks.RichTextBlock()
                )
            ],
            label_format="{title}"
        ),
        collapsed=True,
        max_num=4,
        help_text="Enter a maximum of four highlights"
    )

    class Meta: # noqa
        template = 'streams/highlights.html'
        icon = 'pick'
        label = 'Highlights Block'
