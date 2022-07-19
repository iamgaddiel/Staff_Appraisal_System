# Generated by Django 4.0.5 on 2022-07-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peerperformanceevaluation',
            name='communication',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Satisfactory', 'Satisfactory'), ('Below Average', 'Below Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], help_text='Communicates well with others', max_length=20),
        ),
        migrations.AlterField(
            model_name='peerperformanceevaluation',
            name='efficiency',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Satisfactory', 'Satisfactory'), ('Below Average', 'Below Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], help_text='Efficiency/work flow', max_length=20),
        ),
        migrations.AlterField(
            model_name='peerperformanceevaluation',
            name='good_attitude',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Satisfactory', 'Satisfactory'), ('Below Average', 'Below Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], help_text='comes to work with a good attitude', max_length=20),
        ),
        migrations.AlterField(
            model_name='peerperformanceevaluation',
            name='helpful',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Satisfactory', 'Satisfactory'), ('Below Average', 'Below Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], help_text='Willingness to help others', max_length=20),
        ),
        migrations.AlterField(
            model_name='peerperformanceevaluation',
            name='knowledgeable',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Satisfactory', 'Satisfactory'), ('Below Average', 'Below Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], help_text='Knowledge/skill set in relation to position', max_length=20),
        ),
        migrations.AlterField(
            model_name='peerperformanceevaluation',
            name='punctuality',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Satisfactory', 'Satisfactory'), ('Below Average', 'Below Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], max_length=20),
        ),
        migrations.AlterField(
            model_name='peerperformanceevaluation',
            name='teachability',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Satisfactory', 'Satisfactory'), ('Below Average', 'Below Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], help_text='Willingness to learn', max_length=20),
        ),
        migrations.AlterField(
            model_name='peerperformanceevaluation',
            name='work_by_book',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Satisfactory', 'Satisfactory'), ('Below Average', 'Below Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], help_text='Performs job duties as described in the Employee Handbook', max_length=20),
        ),
    ]