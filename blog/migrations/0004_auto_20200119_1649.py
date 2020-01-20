# Generated by Django 2.2.9 on 2020-01-19 23:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200113_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagerelatedcontent',
            name='url',
        ),
        migrations.AddField(
            model_name='blogpagerelatedcontent',
            name='content',
            field=wagtail.core.fields.StreamField([('link', wagtail.core.blocks.URLBlock()), ('related_content', wagtail.core.blocks.PageChooserBlock()), ('richtext_section', wagtail.core.blocks.RichTextBlock()), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Title for group of cards.', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=100, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Button page will be used first.', required=False))])))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('code_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Name of code block.', required=True)), ('code', wagtail.core.blocks.TextBlock(help_text='Text to be rendered as code.', required=True)), ('language', wagtail.core.blocks.CharBlock(help_text='Programming language.', required=True)), ('caption', wagtail.core.blocks.RichTextBlock(help_text='Brief description of code snippet.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True),
        ),
    ]