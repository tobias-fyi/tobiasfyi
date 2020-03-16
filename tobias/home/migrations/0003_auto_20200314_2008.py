# Generated by Django 3.0.4 on 2020-03-15 02:08

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FyiPage',
            fields=[
                ('homepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.HomePage')),
            ],
            options={
                'abstract': False,
            },
            bases=('home.homepage',),
        ),
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('linkblock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False))])), ('internallinkblock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('plot', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Short title.', max_length=42, required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='Short summary.', max_length=240, required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Long description.', required=False)), ('plot', wagtail.core.blocks.RawHTMLBlock(help_text='HTML code to generate plot.', required=True))])), ('code', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Name of code block.', required=True)), ('code', wagtail.core.blocks.TextBlock(help_text='Text to be rendered as code.', required=True)), ('language', wagtail.core.blocks.CharBlock(help_text='Programming language.', required=True)), ('caption', wagtail.core.blocks.RichTextBlock(help_text='Brief description of code snippet.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]