from django.contrib import admin

# Register your models here.
from .models import (Automobilis,
                     AutomobilioModelis,
                     Paslauga,
                     Uzsakymas,
                     UzsakymoEilute)

class UzsakymoEiluteInLines(admin.TabularInline):
    model = UzsakymoEilute
    extra = 0
class UzsakymasAdmin(admin.ModelAdmin):
    inlines = [UzsakymoEiluteInLines]
    list_display = ("automobilis","data" )

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("automobilio_modelis", "valstybinis_nr", "vin_kodas", "klientas" )

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas","kaina" )



admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(AutomobilioModelis)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute)