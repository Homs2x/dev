# Generated by Django 4.2.7 on 2023-12-16 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_events_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='org_information',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.info'),
        ),
    ]
