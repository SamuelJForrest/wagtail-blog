# Generated by Django 4.2.4 on 2023-08-11 19:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('icon_grid', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=256, required=True)), ('intro_text', wagtail.blocks.CharBlock(max_length=256, required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.RawHTMLBlock(help_text='Paste SVG code here (Make sure to remove strokes from SVG codes.)')), ('title', wagtail.blocks.CharBlock(max_length=256, required=True)), ('text', wagtail.blocks.CharBlock(max_length=1024, required=True))], label_format='{title}'), collapsed=True, max_num=6))]))], blank=True, null=True, use_json_field=True),
        ),
    ]