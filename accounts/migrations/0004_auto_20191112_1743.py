# Generated by Django 2.2.6 on 2019-11-12 14:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191112_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='timezone',
            new_name='time_zone',
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('html', 'HTML'), ('css', 'CSS'), ('js', 'JavaScript'), ('jq', 'JQuery'), ('re', 'React'), ('an', 'Angular'), ('vu', 'Vue'), ('php', 'PHP'), ('lv', 'Laravel'), ('sy', 'Symfony'), ('no', 'Node.js'), ('ex', 'Express.js'), ('my', 'MySQL'), ('ps', 'PostgresQl'), ('md', 'MongoDB'), ('py', 'Python'), ('dj', 'Django'), ('fl', 'Flask'), ('ja', 'Java'), ('c', 'C'), ('cpp', 'C++'), ('cs', 'C#'), ('oc', 'Objective-C'), ('sw', 'Swift'), ('go', 'Go'), ('rs', 'Rust'), ('rb', 'Ruby'), ('rr', 'Ruby On rails')], max_length=87),
        ),
    ]
