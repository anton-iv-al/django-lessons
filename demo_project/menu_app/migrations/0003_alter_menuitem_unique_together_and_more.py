# Generated by Django 5.1.2 on 2024-10-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_alter_menu_menu_label'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menuitem',
            unique_together={('menu', 'title')},
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['menu'], name='menu_app_me_menu_id_a0f054_idx'),
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['menu', 'url'], name='menu_app_me_menu_id_131b4b_idx'),
        ),
    ]