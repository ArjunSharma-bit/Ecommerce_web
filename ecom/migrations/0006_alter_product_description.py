from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
