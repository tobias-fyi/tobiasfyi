# Generated by Django 2.2.9 on 2020-01-19 22:55

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0003_auto_20200113_2109'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField()),
                ('date_begin', models.DateField(verbose_name='Project start date')),
                ('date_end', models.DateField(blank=True, verbose_name='Project completion date')),
                ('repo', models.URLField(blank=True)),
                ('content', wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('code_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Name of code block.', required=True)), ('code', wagtail.core.blocks.TextBlock(help_text='Text to be rendered as code.', required=True)), ('language', wagtail.core.blocks.CharBlock(help_text='Programming language.', required=True)), ('caption', wagtail.core.blocks.RichTextBlock(help_text='Brief description of code snippet.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('related_content', wagtail.core.blocks.PageChooserBlock()), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Title for group of cards.', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=100, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Button page will be used first.', required=False))])))])), ('plot', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Short title for the plot.', max_length=42, required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='Short summary of the plot.', max_length=240, required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Long description of plot.', required=False)), ('plot', wagtail.core.blocks.RawHTMLBlock(help_text='HTML code to generate plot.', required=True))]))])),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogCategory')),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('header_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]