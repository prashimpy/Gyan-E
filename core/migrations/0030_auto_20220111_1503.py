# Generated by Django 3.2.10 on 2022-01-11 15:03

from django.db import migrations
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20220111_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='note_custom',
            field=django_editorjs_fields.fields.EditorJsJSONField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='note_editorjs',
            field=django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True),
        ),
    ]
