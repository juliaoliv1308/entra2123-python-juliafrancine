# Generated by Django 4.2.7 on 2023-11-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angeline', '0007_livro_linkimg_livro_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='estoque',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nota',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='livro',
            name='sub_categoria',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]