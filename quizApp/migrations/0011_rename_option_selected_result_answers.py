# Generated by Django 4.1 on 2022-09-21 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quizApp", "0010_result_passed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="result", old_name="option_selected", new_name="answers",
        ),
    ]