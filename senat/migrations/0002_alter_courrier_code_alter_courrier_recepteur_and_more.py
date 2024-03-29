# Generated by Django 4.1.4 on 2023-07-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courrier',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='recepteur',
            field=models.CharField(choices=[('CABINET DU PRESIDENT DU SENAT', 'CABINET DU PRESIDENT DU SENAT'), ('SECRETARIAT GENERAL', 'SECRETARIAT GENERAL'), ('Sercice des questeurs', 'Sercice des questeurs')], max_length=100),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='service_traitement',
            field=models.CharField(choices=[('Cabinet du président su Sénat(CABPSEN)', 'Cabinet du président su Sénat(CABPSEN)'), ('Sécrétaire Général(SG)', 'Sécrétaire Général(SG)'), ('Sécrétaire Général Adjoint 1(SGA1)', 'Sécrétaire Général Adjoint 1(SGA1)'), ('Sécrétaire Général Adjoint 2(SGA2)', 'Sécrétaire Général Adjoint 2(SGA2)'), ('Conseillé technique(CT)', 'Conseillé technique(CT)'), ('Chargé de mission(CM)', 'Chargé de mission(CM)'), ('Direction des missions internationales(DMI)', 'Direction des missions internationales(DMI)'), ('Direction des servides techniques commun(DSTC)', 'Direction des servides techniques commun(DSTC)'), ('Direction du budget de la solde(DBS)', 'Direction du budget de la solde(DBS)'), ('Direction agence comptable(AC)', 'Direction agence comptable(AC)'), ('Direction des actions sociales et médicales(DASM)', 'Direction des actions sociales et médicales(DASM)'), ("Direction de la traduction de l'interpretation(DTI)", "Direction de la traduction de l'interpretation(DTI)"), ('Direction de la coordination des services ratachés et des relations internationales', 'Direction de la coordination des services ratachés et des relations internationales'), ('Direction de la collectivité territorial décentralisées(DCTD)', 'Direction de la collectivité territorial décentralisées(DCTD)'), ('Direction des ressources humaines(DRH)', 'Direction des ressources humaines(DRH)'), ('Sercice des questeurs', 'Sercice des questeurs')], max_length=150),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='structure',
            field=models.CharField(blank=True, choices=[('SENAT', 'SENAT')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='transmetteur',
            field=models.CharField(choices=[('Cabinet du président su Sénat(CABPSEN)', 'Cabinet du président su Sénat(CABPSEN)'), ('Sécrétaire Général(SG)', 'Sécrétaire Général(SG)'), ('Sécrétaire Général Adjoint 1(SGA1)', 'Sécrétaire Général Adjoint 1(SGA1)'), ('Sécrétaire Général Adjoint 2(SGA2)', 'Sécrétaire Général Adjoint 2(SGA2)'), ('Conseillé technique(CT)', 'Conseillé technique(CT)'), ('Chargé de mission(CM)', 'Chargé de mission(CM)'), ('Direction des missions internationales(DMI)', 'Direction des missions internationales(DMI)'), ('Direction des servides techniques commun(DSTC)', 'Direction des servides techniques commun(DSTC)'), ('Direction du budget de la solde(DBS)', 'Direction du budget de la solde(DBS)'), ('Direction agence comptable(AC)', 'Direction agence comptable(AC)'), ('Direction des actions sociales et médicales(DASM)', 'Direction des actions sociales et médicales(DASM)'), ("Direction de la traduction de l'interpretation(DTI)", "Direction de la traduction de l'interpretation(DTI)"), ('Direction de la coordination des services ratachés et des relations internationales', 'Direction de la coordination des services ratachés et des relations internationales'), ('Direction de la collectivité territorial décentralisées(DCTD)', 'Direction de la collectivité territorial décentralisées(DCTD)'), ('Direction des ressources humaines(DRH)', 'Direction des ressources humaines(DRH)'), ('Sercice des questeurs', 'Sercice des questeurs'), ('AUTRES...', 'AUTRES...')], max_length=150),
        ),
    ]
