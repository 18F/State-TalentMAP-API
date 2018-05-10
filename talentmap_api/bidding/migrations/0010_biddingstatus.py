# Generated by Django 2.0.4 on 2018-04-30 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0017_auto_20180430_1959'),
        ('bidding', '0009_auto_20180409_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiddingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_string_representation', models.TextField(blank=True, help_text='The string representation of this object', null=True)),
                ('status_code', models.CharField(default='OP', help_text='Cycle status code', max_length=120, null=True)),
                ('status', models.CharField(default='Open', help_text='Cycle status text', max_length=120, null=True)),
                ('bidcycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='bidding.BidCycle')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_cycle_statuses', to='position.Position')),
            ],
            options={
                'ordering': ['bidcycle__cycle_start_date'],
                'managed': True,
            },
        ),
    ]
