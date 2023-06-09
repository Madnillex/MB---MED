# Generated by Django 4.1.3 on 2022-12-04 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Kurs', 'verbose_name_plural': 'Kurslar'},
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='courses/', verbose_name='Kurs rasmi'),
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ism')),
                ('lastname', models.CharField(max_length=150, verbose_name='Familiya')),
                ('year', models.IntegerField(default=3, verbose_name='Mutaxasisilik yili')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefon raqami')),
                ('gmail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Telegram')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.course')),
            ],
        ),
    ]
