from django.contrib import admin
from .models import Faction, System, PlayfieldSize, Playfield, POI, PlayfieldPOICount, Resource, DepositSize, PlayfieldResourceCount

admin.site.register(Faction)
admin.site.register(System)
admin.site.register(PlayfieldSize)
admin.site.register(Playfield)
admin.site.register(POI)
admin.site.register(PlayfieldPOICount)
admin.site.register(Resource)
admin.site.register(DepositSize)
admin.site.register(PlayfieldResourceCount)



