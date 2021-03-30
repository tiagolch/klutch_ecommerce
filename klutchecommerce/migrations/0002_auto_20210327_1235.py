# Generated by Django 3.1.7 on 2021-03-27 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klutchecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='produtcts_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtos', to='klutchecommerce.products', verbose_name='Products ID'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
    ]
