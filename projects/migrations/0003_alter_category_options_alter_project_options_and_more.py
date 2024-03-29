# Generated by Django 4.1.3 on 2022-11-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'التصنيف', 'verbose_name_plural': 'التصنيفات'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'مشاريع'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'مهمة', 'verbose_name_plural': 'مهمات'},
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, 'قيد التنفيذ'), (2, 'مكتمل'), (3, 'مؤجل'), (4, 'ملغى')], default=1),
        ),
    ]
