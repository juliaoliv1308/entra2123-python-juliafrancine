# Generated by Django 4.2.7 on 2023-11-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angeline', '0006_delete_categoria_livro_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='linkimg',
            field=models.ImageField(default=0, upload_to='livros/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livro',
            name='pdf',
            field=models.FileField(default=0, upload_to='livros/'),
            preserve_default=False,
        ),
    ]
