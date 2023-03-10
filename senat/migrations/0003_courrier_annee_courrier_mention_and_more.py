# Generated by Django 4.1.3 on 2022-12-07 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senat', '0002_rename_reciever_courrier_recepteur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courrier',
            name='annee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='courrier',
            name='mention',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='courrier',
            name='service_traitement',
            field=models.CharField(choices=[('Direction de la coordination des services ratachés et des relations internationales', 'Direction de la coordination des services ratachés et des relations internationales'), ('Direction de l agence comptable du service de la comptabilité matière et du bureau de liaison à l etrnager', 'Direction de l agence comptable du service de la comptabilité matière et du bureau de liaison à l etrnager'), ('Direction de la legislation, du contrôle parlementaire et des services linguistique', 'Direction de la legislation, du contrôle parlementaire et des services linguistique'), ('Direction du budget et de la solde(DBS)', 'Direction du budget et de la solde(DBS)'), ('Direction des relations(DRH)', 'Direction des relations(DRH)'), ('Direction des actions sociales et médicales(DASM)', 'Direction des actions sociales et médicales(DASM)'), ('Direction des servides techniques commun(DSTC)', 'Direction des servides techniques commun(DSTC)'), ('Direction de la documentation, des archives et de la recherche parlementaire(DDARP)', 'Direction de la documentation, des archives et de la recherche parlementaire(DDARP)'), ('Inspecteurs généraux(IG)', 'Inspecteurs généraux(IG)'), ('Direction des relations(DRH)', 'Direction des relations(DRH)'), ('Sécrétaire particulier(SP)', 'Sécrétaire particulier(SP)'), ('Conseillé technique(CT)', 'Conseillé technique(CT)'), ('Chargé de mission(CM)', 'Chargé de mission(CM)'), ('Chargé d études(CE)', 'Chargé d études(CE)'), ('Chargé d études assistante(CE)', 'Chargé d études assistante(CE)')], default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courrier',
            name='structure',
            field=models.CharField(choices=[('SENAT', 'SENAT'), ('UNIVERSITE DE YAOUNDE 1', 'UNIVERSITE DE YAOUNDE 1')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courrier',
            name='types',
            field=models.CharField(choices=[('LETTRE(L)', 'LETTRE(L)'), ('REQUETE(R)', 'REQUETE(R)'), ('LOI(LN)', 'LOI(LN)'), ('DECISION(D)', 'DECISION(D)'), ('NOTE(N)', 'NOTE(N)'), ('PROJET DE LOI(PJL)', 'PROJET DE LOI(PJL)'), ('PROPOSITION DE LOI(PL)', 'PROPOSITION DE LOI(PL)'), ('ARRETE DE BUREAU(AB)', 'ARRETE DE BUREAU(AB)')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courrier',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='recepteur',
            field=models.CharField(choices=[('CABINET DU PRESIDENT DU SENAT', 'CABINET DU PRESIDENT DU SENAT'), ('SECRETARIAT GENERAL', 'SECRETARIAT GENERAL'), ('DECANT', 'DECANT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='transmetteur',
            field=models.CharField(choices=[('Direction de la coordination des services ratachés et des relations internationales', 'Direction de la coordination des services ratachés et des relations internationales'), ('Direction de l agence comptable du service de la comptabilité matière et du bureau de liaison à l etrnager', 'Direction de l agence comptable du service de la comptabilité matière et du bureau de liaison à l etrnager'), ('Direction de la legislation, du contrôle parlementaire et des services linguistique', 'Direction de la legislation, du contrôle parlementaire et des services linguistique'), ('Direction du budget et de la solde(DBS)', 'Direction du budget et de la solde(DBS)'), ('Direction des relations(DRH)', 'Direction des relations(DRH)'), ('Direction des actions sociales et médicales(DASM)', 'Direction des actions sociales et médicales(DASM)'), ('Direction des servides techniques commun(DSTC)', 'Direction des servides techniques commun(DSTC)'), ('Direction de la documentation, des archives et de la recherche parlementaire(DDARP)', 'Direction de la documentation, des archives et de la recherche parlementaire(DDARP)'), ('Inspecteurs généraux(IG)', 'Inspecteurs généraux(IG)'), ('Direction des relations(DRH)', 'Direction des relations(DRH)'), ('Sécrétaire particulier(SP)', 'Sécrétaire particulier(SP)'), ('Conseillé technique(CT)', 'Conseillé technique(CT)'), ('Chargé de mission(CM)', 'Chargé de mission(CM)'), ('Chargé d études(CE)', 'Chargé d études(CE)'), ('Chargé d études assistante(CE)', 'Chargé d études assistante(CE)')], max_length=150),
        ),
    ]
