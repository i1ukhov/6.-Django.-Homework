# Generated by Django 3.2.25 on 2024-05-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите заголовок', max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(help_text='Добавьте слаг', max_length=150, verbose_name='Слаг')),
                ('content', models.TextField(help_text='Добавьте содержимое', verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='blog/images', verbose_name='Превью')),
                ('created_at', models.DateField(help_text='Добавьте дату создания', verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, help_text='Опубликовать запись', verbose_name='Опубликовано?')),
                ('views_count', models.IntegerField(blank=True, default=0, help_text='Добавьте количество просмотров', null=True, verbose_name='Количество просмотров')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(help_text='Добавьте цену продукта', verbose_name='Цена'),
        ),
    ]
