# Generated by Django 3.2.6 on 2021-09-11 22:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_core", "0028_alter_token_intent"),
        ("authentik_events", "0017_alter_event_action"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationWebhookMapping",
            fields=[
                (
                    "propertymapping_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_core.propertymapping",
                    ),
                ),
            ],
            options={
                "verbose_name": "Notification Webhook Mapping",
                "verbose_name_plural": "Notification Webhook Mappings",
            },
            bases=("authentik_core.propertymapping",),
        ),
        migrations.AddField(
            model_name="notificationtransport",
            name="webhook_mapping",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="authentik_events.notificationwebhookmapping",
            ),
        ),
    ]