from django.contrib import admin
from Modules.Academical.models import *

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Usuario)
admin.site.register(Personal)
admin.site.register(SignosVitales)
admin.site.register(Historia_Clinica)
admin.site.register(Citas)
admin.site.register(Sugerencia)


