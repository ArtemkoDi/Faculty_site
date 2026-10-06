import re
from django.db import migrations

def clean_places_to_numbers(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty_fen', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        match = re.search(r'\d+', program.places)
        if match:
            program.places = match.group()
        program.save()

def restore_places_text(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty_fen', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        program.places = f"{program.places} місць"
        program.save()

class Migration(migrations.Migration):

    dependencies = [
        ('faculty_fen', '0007_auto_20261006_1143'),
    ]

    operations = [
        migrations.RunPython(
            code=clean_places_to_numbers,
            reverse_code=restore_places_text
        )
    ]
