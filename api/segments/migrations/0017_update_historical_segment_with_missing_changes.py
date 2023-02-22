# Generated by Django 3.2.16 on 2023-02-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0016_add_historical_records_to_segment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalsegment',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical segment', 'verbose_name_plural': 'historical segments'},
        ),
        migrations.AlterField(
            model_name='historicalsegment',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]