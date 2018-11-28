from django.db import models


#dejar las constraint not null para evitar errores

# Create your models here.



#tablas Cris

class Region(models.Model):
    descripcion=models.CharField(max_length=30)

    class Meta:
        verbose_name="Region"
        verbose_name_plural="Regiones"
    def __str__(self):
        return self.descripcion



class Comuna(models.Model):
    descripcionComuna=models.CharField(max_length=30)
    idregion = models . ForeignKey ( Region , on_delete = models . CASCADE )

    class Meta:
        verbose_name="Comuna"
        verbose_name_plural="Comunas"

    def __str__(self):
        return self.descripcionComuna




class Tipo_Vivienda(models.Model):
    descripcionVivienda=models.CharField(max_length=44)
    
    class Meta:
        verbose_name_plural="Tipos de Vivienda"

    def __str__(self):
        return self.descripcionVivienda



class Tipo_usuario(models.Model):
    descripcionUsuario=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="Tipos de Usuario"

    def __str__(self):
        return self.descripcionUsuario



class Usuario(models.Model):
    rut_usuario=models.CharField(max_length=20)
    nombre=models.CharField(max_length=100)
    ap_pat=models.CharField(max_length=100)
    ap_mat=models.CharField(max_length=100)
    fec_nac=models.DateField()
    telefon=models.IntegerField()
    direccion=models.CharField(max_length=255)
    mail=models.CharField(max_length=50)
    id_usuario=models.ForeignKey(Tipo_usuario,on_delete=models.CASCADE)
    id_tip_vivienda=models.ForeignKey(Tipo_Vivienda,on_delete=models.CASCADE)
    id_comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE)
    id_genero=models.CharField(max_length=10)


    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"

    def __str__(self):
        return self.rut_usuario



class Trabajador(models.Model):
    rut_trabajador=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    ap_pat=models.CharField(max_length=100)
    ap_mat=models.CharField(max_length=100)
    fec_nac=models.DateField()
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=255)
    mail=models.CharField(max_length=50)
    sueldo=models.IntegerField()
    id_comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE,null=True)
    id_genero=models.CharField(max_length=10)

    class Meta:
        verbose_name="Trabajador"
        verbose_name_plural="Trabajadores"

    def __str__(self):
        return self.rut_trabajador



class Login(models.Model):
    usuario=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    rut_trabajador=models.ForeignKey(Trabajador,on_delete=models.CASCADE,null=True)
    rut_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)


    class Meta:
        verbose_name="Login"
        verbose_name_plural="Login"

    def __str__(self):
        return self.usuario 



class Fondo_Economico(models.Model):
    monto_ahorro=models.IntegerField()

    class Meta:
        verbose_name="Fondo Economico"
        verbose_name_plural="Fondos Economicos"

    def __str__(self):
        return self.monto_ahorro 



class Tipo_insumo(models.Model):
    descripcionInsumo=models.CharField(max_length=15)


    class Meta:
        verbose_name="Tipo Insumo"
        verbose_name_plural="Tipos de Insumo"

    def __str__(self):
        return self.descripcionInsumo 



class Transferencia(models.Model):
    rut_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    id_fondo=models.ForeignKey(Fondo_Economico,on_delete=models.CASCADE,null=True)
    cod_compania=models.IntegerField()
    
    class Meta:
        verbose_name="Transferencia"
        verbose_name_plural="Transferencias"

    def __str__(self):
        return self.rut_usuario 


class Insumo(models.Model):
    descripcion=models.CharField(max_length=100)
    id_tip_insumo=models.ForeignKey(Tipo_insumo,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name="Insumo"
        verbose_name_plural="Insumos"

    def __str__(self):
        return self.descripcion



class Refugio(models.Model):
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)

    class Meta:
        verbose_name="Refugio"
        verbose_name_plural="Refugios" 

    def __str__(self):
        return self.nombre


class Raza(models.Model):
    descripcion=models.CharField(max_length=100)

    class Meta:
        verbose_name="Raza"
        verbose_name_plural="Razas" 

    def __str__(self):
        return self.descripcion


class Origen_mascota(models.Model):
    descripcion=models.CharField(max_length=10)

    class Meta:
        verbose_name="Origen mascota"
        verbose_name_plural="Origen de mascotas" 

    def __str__(self):
        return self.descripcion


class Mascota(models.Model):
    nombre=models.CharField(max_length=100)
    esterilizado=models.CharField(max_length=1)
    chip=models.CharField(max_length=1)
    fec_nac=models.DateField()
    id_raza=models.ForeignKey(Raza,on_delete=models.CASCADE,null=True)
    id_orig_masc=models.ForeignKey(Origen_mascota,on_delete=models.CASCADE,null=True)
    cod_refugio=models.ForeignKey(Refugio,on_delete=models.CASCADE,null=True)
    rut_usuario=models.CharField(max_length=20)
    imagen=models.ImageField(upload_to="mascotas",null=True)

    def fecNaMa(self):
        return self.fec_nac.strftime("%Y-%m-%d")

    class Meta:
        verbose_name="Mascota"
        verbose_name_plural="Mascotas" 

    def __str__(self):
        return self.nombre



#ver como modificar para rescatar la hora
class Visita_Medica(models.Model):
    fec_visita=models.DateField()
    hora=models.DateTimeField()
    minuto=models.DateTimeField()
    rut_trabajador=models.ForeignKey(Trabajador,on_delete=models.CASCADE,null=True)
    cod_mascota=models.ForeignKey(Mascota,on_delete=models.CASCADE,null=True)
    
    class Meta:
        verbose_name="Visita Medica"
        verbose_name_plural="Visitas Medicas" 

    def __str__(self):
        return self.fec_visita



class Tipo_campania(models.Model):
    descripcion=models.CharField(max_length=50)

    class Meta:
        verbose_name="Tipo campaña"
        verbose_name_plural="Tipos de campaña" 

    def __str__(self):
        return self.descripcion


class Campania(models.Model):
    nombre=models.CharField(max_length=100)
    eslogan=models.CharField(max_length=255)
    fec_campania=models.DateField()
    horario=models.IntegerField()
    id_tip_campania=models.ForeignKey(Tipo_campania,on_delete=models.CASCADE,null=True)


    class Meta:
        verbose_name="Campaña"
        verbose_name_plural="Campañas" 

    def __str__(self):
        return self.nombre




class Campania_insumo(models.Model):
    cod_campania=models.ForeignKey(Campania,on_delete=models.CASCADE,null=True)
    id_insumo=models.ForeignKey(Insumo,on_delete=models.CASCADE,null=True)
    cantidad=models.IntegerField()


    class Meta:
        verbose_name="Campaña insumo"
        verbose_name_plural="Campañas de insumos" 

    def __str__(self):
        return self.cod_campania


class Visita_adopcion(models.Model):
    adopcion=models.CharField(max_length=1)
    rut_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    cod_mascota=models.ForeignKey(Mascota,on_delete=models.CASCADE,null=True)
    cod_compania=models.ForeignKey(Campania,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name="Visita adopcion"
        verbose_name_plural="Visitas de adopcion" 

    def __str__(self):
        return self.adopcion

