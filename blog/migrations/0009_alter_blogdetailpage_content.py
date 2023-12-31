# Generated by Django 4.2.4 on 2023-08-17 05:54

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogdetailpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.fields.StreamField([('icon_grid', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=256, required=True)), ('intro_text', wagtail.blocks.CharBlock(max_length=256, required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.RawHTMLBlock(help_text='Paste SVG code here (Make sure to remove strokes from SVG codes.)')), ('title', wagtail.blocks.CharBlock(max_length=256, required=True)), ('text', wagtail.blocks.CharBlock(max_length=1024, required=True))], label_format='{title}'), collapsed=True, max_num=6))])), ('rich_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('highlights', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(blank=True, max_length=256)), ('content', wagtail.blocks.RichTextBlock())], label_format='{title}'), collapsed=True, help_text='Enter a maximum of four highlight', max_num=4))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
