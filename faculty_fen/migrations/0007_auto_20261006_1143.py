from django.db import migrations


def split_university_and_country(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty_fen', 'ExchangeProgram')

    for program in ExchangeProgram.objects.all():
        text = program.university
        uni = text
        country = ""

        if '(' in text and ')' in text:
            uni, country = text.split('(')
            country = country.replace(')', '')
        elif ',' in text:
            uni, country = text.split(',')
        elif '-' in text:
            uni, country = text.split('-')

        program.university = uni.strip()
        program.country = country.strip()
        program.save()


def merge_university_and_country(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty_fen', 'ExchangeProgram')

    for program in ExchangeProgram.objects.all():
        if program.country:
            program.university = f"{program.university}, {program.country}"
            program.country = ""
            program.save()


class Migration(migrations.Migration):
    dependencies = [
        ('faculty_fen', '0006_exchangeprogram_country'),
    ]

    operations = [
        migrations.RunPython(
            code=split_university_and_country,
            reverse_code=merge_university_and_country
        )
    ]
