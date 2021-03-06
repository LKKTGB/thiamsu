# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 18:25
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("thiamsu", "0009_headline")]

    operations = [
        migrations.AlterModelOptions(
            name="headline",
            options={"verbose_name": "headline", "verbose_name_plural": "headlines"},
        ),
        migrations.AlterModelOptions(
            name="newword",
            options={"verbose_name": "new_word", "verbose_name_plural": "new_words"},
        ),
        migrations.AlterModelOptions(
            name="song",
            options={"verbose_name": "song", "verbose_name_plural": "songs"},
        ),
        migrations.AlterModelOptions(
            name="translation",
            options={
                "verbose_name": "translation",
                "verbose_name_plural": "translations",
            },
        ),
        migrations.AlterField(
            model_name="approvedtranslation",
            name="lang",
            field=models.CharField(
                choices=[
                    ("tailo", "translation_lang_tailo"),
                    ("hanzi", "translation_lang_hanzi"),
                ],
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="headline",
            name="end_time",
            field=models.DateTimeField(verbose_name="headline_end_time"),
        ),
        migrations.AlterField(
            model_name="headline",
            name="song",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="thiamsu.Song",
                verbose_name="song",
            ),
        ),
        migrations.AlterField(
            model_name="headline",
            name="start_time",
            field=models.DateTimeField(verbose_name="headline_start_time"),
        ),
        migrations.AlterField(
            model_name="newword",
            name="content",
            field=models.CharField(max_length=100, verbose_name="new_word_content"),
        ),
        migrations.AlterField(
            model_name="newword",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="new_word_created_at"
            ),
        ),
        migrations.AlterField(
            model_name="newword",
            name="reference_url",
            field=models.CharField(
                max_length=100, verbose_name="new_word_reference_url"
            ),
        ),
        migrations.AlterField(
            model_name="newword",
            name="song",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="thiamsu.Song",
                verbose_name="song",
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="composer",
            field=models.CharField(max_length=100, verbose_name="song_composer"),
        ),
        migrations.AlterField(
            model_name="song",
            name="hanlo_performer",
            field=models.CharField(max_length=100, verbose_name="song_hanlo_performer"),
        ),
        migrations.AlterField(
            model_name="song",
            name="hanlo_title",
            field=models.CharField(max_length=100, verbose_name="song_hanlo_title"),
        ),
        migrations.AlterField(
            model_name="song",
            name="hanzi_title",
            field=models.CharField(max_length=100, verbose_name="song_hanzi_title"),
        ),
        migrations.AlterField(
            model_name="song",
            name="lyricist",
            field=models.CharField(max_length=100, verbose_name="song_lyricist"),
        ),
        migrations.AlterField(
            model_name="song",
            name="original_lyrics",
            field=models.TextField(default="", verbose_name="song_original_lyrics"),
        ),
        migrations.AlterField(
            model_name="song",
            name="original_title",
            field=models.CharField(max_length=100, verbose_name="song_original_title"),
        ),
        migrations.AlterField(
            model_name="song",
            name="performer",
            field=models.CharField(max_length=100, verbose_name="song_performer"),
        ),
        migrations.AlterField(
            model_name="song",
            name="readonly",
            field=models.BooleanField(default=False, verbose_name="song_readonly"),
        ),
        migrations.AlterField(
            model_name="song",
            name="tailo_title",
            field=models.CharField(max_length=100, verbose_name="song_tailo_title"),
        ),
        migrations.AlterField(
            model_name="song",
            name="youtube_url",
            field=models.CharField(max_length=100, verbose_name="song_youtube_url"),
        ),
        migrations.AlterField(
            model_name="translation",
            name="content",
            field=models.CharField(max_length=1000, verbose_name="translation_content"),
        ),
        migrations.AlterField(
            model_name="translation",
            name="contributor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="translation_contributor",
            ),
        ),
        migrations.AlterField(
            model_name="translation",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="translation_created_at"
            ),
        ),
        migrations.AlterField(
            model_name="translation",
            name="lang",
            field=models.CharField(
                choices=[
                    ("tailo", "translation_lang_tailo"),
                    ("hanzi", "translation_lang_hanzi"),
                ],
                max_length=5,
                verbose_name="translation_lang",
            ),
        ),
        migrations.AlterField(
            model_name="translation",
            name="line_no",
            field=models.PositiveSmallIntegerField(verbose_name="translation_line_no"),
        ),
        migrations.AlterField(
            model_name="translation",
            name="song",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="thiamsu.Song",
                verbose_name="song",
            ),
        ),
    ]
