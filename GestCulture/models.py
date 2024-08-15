from django.db import models

# Create your models here.
class DonneeMeteo(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidite = models.FloatField()
    actif = models.BooleanField(default=True)

    def consulter_donnees_meteo(self):
        return DonneeMeteo.objects.all()

class Agriculteur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    actif = models.BooleanField(default=True)

    def s_authentifier(self):
        # Code pour l'authentification
        pass

    def creer_profil(self):
        # Code pour créer un profil
        pass

    def mise_a_jour_profil(self):
        # Code pour mettre à jour le profil
        pass

class Culture(models.Model):
    nom = models.CharField(max_length=100)
    date_plantation = models.DateField()
    date_recolte = models.DateField()
    agriculteur = models.ForeignKey(Agriculteur, on_delete=models.CASCADE)
    actif = models.BooleanField(default=True)

    def ajouter_culture(self):
        # Code pour ajouter une culture
        pass

    def supprimer_culture(self):
        # Code pour supprimer une culture
        pass

    def modifier_culture(self):
        # Code pour modifier une culture
        pass

class CalendrierPlantation(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    actif = models.BooleanField(default=True)

    def consulter_calendrier(self):
        return CalendrierPlantation.objects.all()

class MethodeGestion(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    details = models.TextField()
    actif = models.BooleanField(default=True)

    def enregistrer_methode(self):
        # Code pour enregistrer une méthode de gestion
        pass

class Stock(models.Model):
    produit = models.CharField(max_length=100)
    quantite = models.IntegerField()
    date_entree = models.DateField()
    actif = models.BooleanField(default=True)

    def gerer_stock(self):
        # Code pour gérer le stock
        pass

class Vente(models.Model):
    produit = models.CharField(max_length=100)
    quantite = models.IntegerField()
    date_vente = models.DateField()
    prix = models.FloatField()
    actif = models.BooleanField(default=True)

    def enregistrer_vente(self):
        # Code pour enregistrer une vente
        pass

class RapportAnalyse(models.Model):
    type = models.CharField(max_length=100)
    date_generation = models.DateField()
    contenu = models.TextField()
    actif = models.BooleanField(default=True)

    def generer_rapport(self):
        # Code pour générer un rapport
        pass

    class Meta:
        verbose_name = ("DonneeMeteo")
        verbose_name_plural = ("DonneeMeteos")
        verbose_name = ("Agriculteur")
        verbose_name_plural = ("Agriculteurs")
        verbose_name = ("culture")
        verbose_name_plural = ("cultures")
        verbose_name = ("calendrierPlantation")
        verbose_name_plural = ("calendrierPlantations")
        verbose_name = ("MethodeGestion")
        verbose_name_plural = ("MethodeGestions")
        verbose_name = ("stock")
        verbose_name_plural = ("stocks")
        verbose_name = ("vente")
        verbose_name_plural = ("ventes")
        verbose_name = ("RapportAnalyse")
        verbose_name_plural = ("RapportAnalyses")
        
        def __str__(self):
            return self.name