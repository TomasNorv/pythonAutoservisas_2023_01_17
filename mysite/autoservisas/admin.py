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

class UzsakymoEiluteAdmin(admin.ModelAdmin):
      list_display = ("uzsakymas", "paslauga", "kiekis", "kaina")


class UzsakymasAdmin(admin.ModelAdmin):
    inlines = [UzsakymoEiluteInLines]
    list_display = ("automobilis", "data", "suma")

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("automobilio_modelis", "valstybinis_nr", "vin_kodas", "klientas" )
    list_filter = ("klientas", "automobilio_modelis")
    search_fields = ("valstybinis_nr", "vin_kodas")
class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas","kaina" )

class AutomobilioModelisAdmin(admin.ModelAdmin):
     list_display = ("marke", "modelis")



admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(AutomobilioModelis, AutomobilioModelisAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute, UzsakymoEiluteAdmin)


