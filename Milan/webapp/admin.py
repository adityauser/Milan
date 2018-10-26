from django.contrib import admin

from webapp.models import Lost,Found,idlost,idfound
#LostId,FoundId

# Register your models here.
admin.site.register(Lost)
admin.site.register(Found)
admin.site.register(idfound)
admin.site.register(idlost)
