from django.db import models

# Create your models here.
class Usuario (models.Model):
	ID_User = models.CharField(max_length=4, primary_key=True)
	Nombre = models.CharField(max_length=45)
	Contraseña = models.CharField(max_length=8)
	Tiusuarios = [
		('M', 'Medico(a)'),
		('E', 'Enfermera(o)'),
		('A', 'Auxiliar'),
		('P', 'Paciente')
	]
	Tipo_Usuarios=models.CharField(max_length=1, choices=Tiusuarios, default='P')

	def __str__(self):
		txt = "{0} Nombre: {1} / {2}"
		return txt.format(self.ID_User,self.Nombre, self.Tipo_Usuarios)

class Personal(models.Model):
    ID_PS = models.CharField(max_length=4, primary_key=True)
    Nombre = models.CharField(max_length=45)
    Especialidad = models.CharField(max_length=45, default='No Aplica')
    Tipersonal = [
        ('M', 'Medico(a)'),
		('E', 'Enfermera(o)'),
		('A', 'Auxiliar')
        ]
    Tipo_personal = models.CharField(max_length=1, choices=Tipersonal, default='M')
    ID_UserPS = models.ForeignKey(Usuario,null=True,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0} Nombre: {1} / {2}"
        return txt.format(self.ID_PS,self.Nombre, self.Tipo_personal)

class Paciente(models.Model):
    idPaciente =  models.CharField(max_length=4, primary_key=True)
    nombre =  models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    fechaNacimiento = models.DateField()
    edad = models.CharField(max_length=3)
    RH = models.CharField(max_length=2)
    correo = models.EmailField (max_length=45)
    celular = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    internado = models.BooleanField(default=True)
    nombreFamiliar = models.CharField(max_length=45)
    parentescoFamiliar = models.CharField(max_length=45)
    correoFamiliar = models.EmailField (max_length=45)
    celularFamiliar = models.CharField (max_length=45)
    ID_UserP = models.ForeignKey(Usuario,null=True,blank=False,on_delete=models.CASCADE)

    def __str__ (self):
        txt = "{0} {1} {2} esta internado"
        if self.internado:
            estadoEstudiante = "Activo"
        else:
            estadoEstudiante = "InActivo"
        return txt.format(self.idPaciente,self.nombre, self.apellidos)

class SignosVitales(models.Model):
    IDSV = models.AutoField(primary_key=True)
    IDPaciente=models.ForeignKey(Paciente,null=False,blank=False,on_delete=models.CASCADE)
    fechaSV=models.DateTimeField()
    presionArterial=models.IntegerField(max_length=3)
    temperatura=models.FloatField(null=True)
    oximetria=models.IntegerField(max_length=3)
    frecuenciaRespiratoria=models.IntegerField(max_length=3)
    frecuenciaCardiaca=models.IntegerField(max_length=3)
    glicemias=models.IntegerField(max_length=3)

    def __str__ (self):
        txt="{0} tiene signos vitales"
        return txt.format(self.IDPaciente)


class Historia_Clinica(models.Model):
    Consecutivo = models.AutoField(primary_key=True)
    Diagnostico = models.CharField(max_length=200)
    ID_PS=models.ForeignKey(Personal,null=False,blank=False,on_delete=models.CASCADE)
    ID_SV=models.ForeignKey(SignosVitales,null=False,blank=False,on_delete=models.CASCADE)
    ID=models.ForeignKey(Paciente,null=False,blank=False,on_delete=models.CASCADE)

    def __str__ (self):
        txt = "HC #{0} - Paciente:{1}"
        return txt.format(self.Consecutivo,self.ID)

class Citas(models.Model):
    Consecutivo_Cita = models.AutoField(primary_key=True)
    Especialidad = models.CharField(max_length=45)
    Motivo = models.CharField(max_length=45)
    Fecha_Hora= models.DateTimeField()
    Consecutivo_HC=models.ForeignKey(Historia_Clinica,null=False,blank=False,on_delete=models.CASCADE)
    ID=models.ForeignKey(Paciente,null=False,blank=False,on_delete=models.CASCADE)
    ID_PS=models.ForeignKey(Personal,null=False,blank=False,on_delete=models.CASCADE)

    def __str__ (self):
        txt = "Cita #{0} - Paciente:{1}"
        return txt.format(self.Consecutivo_Cita,self.ID)

class Sugerencia(models.Model):
    Consecutivo = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=200)
    ID_PS=models.ForeignKey(Personal,null=True,blank=False,on_delete=models.CASCADE)
    Fecha_registro = models.DateTimeField()
    Consecutivo_HC=models.ForeignKey(Historia_Clinica,null=False,blank=False,on_delete=models.CASCADE)


    def __str__ (self):
        txt = "Sugerencia #{0}"
        return txt.format(self.Consecutivo)








