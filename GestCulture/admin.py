from django.contrib import admin
from .models import Agriculteur,DonneeMeteo,CalendrierPlantation,Culture,MethodeGestion,Stock,Vente,RapportAnalyse

# Register your models here.
class AdminDonneeMeteo(admin.ModelAdmin):
    list_display = ('date','temperature','humidite','actif')
class AdminAgriculteur(admin.ModelAdmin):
    list_display = ('nom','email','mot_de_passe','adresse','telephone','actif')
class AdminCulture(admin.ModelAdmin):
    list_display = ('nom','date_plantation','date_recolte','actif')
class AdminCalendrierPlantation(admin.ModelAdmin):
    list_display = ('culture','date_debut','date_fin','actif')
class AdminMethodeGestion(admin.ModelAdmin):
    list_display = ('culture','type','details','actif')
class AdminStock(admin.ModelAdmin):
    list_display = ('produit','quantite','date_entree','actif')
class Adminvente(admin.ModelAdmin):
    list_display = ('produit','quantite','date_vente','prix','actif')
class AdminRapportAnalyse(admin.ModelAdmin):
    list_display = ('type','date_generation','contenu','actif')


admin.site.register(DonneeMeteo, AdminDonneeMeteo)
admin.site.register(Agriculteur, AdminAgriculteur)
admin.site.register(Culture, AdminCulture)
admin.site.register(CalendrierPlantation, AdminCalendrierPlantation)
admin.site.register(MethodeGestion, AdminMethodeGestion)
admin.site.register(Stock, AdminStock)
admin.site.register(Vente, Adminvente)
admin.site.register(RapportAnalyse, AdminRapportAnalyse)
