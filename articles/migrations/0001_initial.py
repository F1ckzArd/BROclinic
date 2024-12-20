
from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='docs_images', verbose_name='Image')),
                ('content', martor.models.MartorField(verbose_name='Content')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
