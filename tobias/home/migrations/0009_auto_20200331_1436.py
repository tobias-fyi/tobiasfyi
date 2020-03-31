# Generated by Django 3.0.4 on 2020-03-31 20:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200331_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock()), ('title_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Title content', required=True)), ('permalink', wagtail.core.blocks.CharBlock(help_text='HTML class for permalink', required=False))])), ('section_header', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(help_text='Header content', required=True)), ('permalink', wagtail.core.blocks.CharBlock(help_text='HTML class for permalink', required=False))])), ('featured_section', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(help_text='Title to display above the featured section', max_length=255, required=False)), ('permalink', wagtail.core.blocks.CharBlock(help_text='HTML class for permalink', required=False)), ('featured_section', wagtail.core.blocks.PageChooserBlock(help_text='First featured section for the homepage. Will display up to three child items.', required=False))])), ('image_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Short title.', max_length=42, required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='Short summary.', max_length=240, required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Long description.', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('linkblock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False))])), ('internallinkblock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('button', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False))])), ('plot', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Short title.', max_length=42, required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='Short summary.', max_length=240, required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Long description.', required=False)), ('plot', wagtail.core.blocks.RawHTMLBlock(help_text='HTML code to generate plot.', required=True))])), ('code', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Name of code block.', required=True)), ('code', wagtail.core.blocks.TextBlock(help_text='Text to be rendered as code.', required=True)), ('language', wagtail.core.blocks.CharBlock(help_text='Programming language.', required=True)), ('caption', wagtail.core.blocks.RichTextBlock(help_text='Brief description of code snippet.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], null=True),
        ),
    ]
