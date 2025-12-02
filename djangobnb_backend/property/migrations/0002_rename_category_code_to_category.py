from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='category_code',
            new_name='category',
        ),
    ]
