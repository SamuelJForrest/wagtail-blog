# Generated by Django 4.2.4 on 2023-08-12 21:27

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='Overwrites default title', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='Overwrites default title', max_length=100)),
                ('content', wagtail.fields.StreamField([('icon_grid', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=256, required=True)), ('intro_text', wagtail.blocks.CharBlock(max_length=256, required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.RawHTMLBlock(help_text='Paste SVG code here (Make sure to remove strokes from SVG codes.)')), ('title', wagtail.blocks.CharBlock(max_length=256, required=True)), ('text', wagtail.blocks.CharBlock(max_length=1024, required=True))], label_format='{title}'), collapsed=True, max_num=6))]))], blank=True, null=True, use_json_field=True)),
                ('banner_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]