# Generated by Django 3.2.12 on 2022-04-22 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20220413_1829'),
        ('rating', '0008_alter_rating_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='catalog.item', verbose_name='Товар'),
        ),
    ]
