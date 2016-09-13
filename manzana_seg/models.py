from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Manzana_seg(models.Model):
    ubigeo = models.CharField(max_length=255)
    zona = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True)
    aeu = models.CharField(max_length=255, blank=True)
    aeu_seccion = models.CharField(max_length=255, blank=True)
    aeu_zona = models.CharField(max_length=255, blank=True)
    aeu_viv = models.CharField(max_length=255, blank=True)
    aer_ini = models.CharField(max_length=255, blank=True)
    aer_fin = models.CharField(max_length=255, blank=True)
    estado_seg = models.CharField(max_length=255, blank=True)
    estado_rep = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return '%s , %s' % (self.ubigeo, self.zona)

    class Meta:
        managed = False
        db_table = 'MANZANA_SEG'


class Segmentacion_prueba(models.Model):
    cod_dd = models.IntegerField(primary_key=True)
    departamento = models.CharField(max_length=50)
    cod_prov = models.IntegerField()
    provincia = models.CharField(max_length=50)
    cod_dis = models.IntegerField()
    distrito = models.CharField(max_length=50)
    zona = models.CharField(max_length=5)
    seccion = models.CharField(max_length=18)
    codccpp = models.CharField(max_length=4)
    cat_ccpp = models.CharField(max_length=2)
    aeu_n = models.CharField(max_length=3)
    nro_aeu = models.IntegerField()
    estado_seg = models.IntegerField()
    estado_croquis = models.IntegerField()

    def __unicode__(self):
        return '%s , %s' % (self.departamento, self.provincia)

    class Meta:
        managed = False
        db_table = 'TEMPORAL'


#Clases validadas
class Departamento(models.Model):
    ccdd = models.CharField(db_column='CCDD',max_length=2, primary_key=True)
    departamento = models.CharField(db_column='DEPARTAMENTO', blank=True, null=True,max_length=50)
    fec_carga = models.DateTimeField(db_column='FEC_CARGA', blank=True, null=True)
    
    def __unicode__(self):
        return '%s , %s' % (self.ccdd, self.departamento)

    class Meta:
        managed = False
        db_table = 'TB_DEPARTAMENTO'


class Provincia(models.Model):
    ccdd = models.ForeignKey(Departamento, db_column='CCDD')
    ccpp = models.CharField(db_column='CCPP', max_length=2, primary_key=True)
    cod_prov = models.CharField(db_column='COD_PROV', max_length=4, blank=True, null=True)
    provincia = models.CharField(db_column='PROVINCIA', max_length=50, blank=True, null=True)
    fec_carga = models.DateTimeField(db_column='FEC_CARGA', blank=True, null=True)
   
    def __unicode__(self):
        return '%s , %s' % (self.ccpp, self.provincia)

    class Meta:
        managed = False
        db_table = 'TB_PROVINCIA'
        unique_together = (('ccdd', 'ccpp'))

class Distrito(models.Model):
    ubigeo = models.CharField(db_column='UBIGEO', max_length=6, primary_key=True)
    ccdd = models.ForeignKey(Departamento, db_column='CCDD')
    ccpp = models.ForeignKey(Provincia, db_column='CCPP')
    ccdi = models.CharField(db_column='CCDI', max_length=2, primary_key=True)
    distrito = models.CharField(db_column='DISTRITO', max_length=50, blank=True, null=True)
    region = models.CharField(db_column='REGION', max_length=50, blank=True, null=True)
    region_nat = models.CharField(db_column='REGION_NAT', max_length=50, blank=True, null=True)
    nro_aer = models.CharField(db_column='NRO_AER', max_length=50, blank=True, null=True)
    fec_carga = models.DateTimeField(db_column='FEC_CARGA', blank=True, null=True)
    
    def __unicode__(self):
        return '%s , %s' % (self.ccdd, self.departamento)

    class Meta:
        managed = False
        db_table = 'TB_DISTRITO'
        unique_together = (('ubigeo', 'ccdd', 'ccpp', 'ccdi'))

class Zona(models.Model):
    ubigeo = models.ForeignKey(Distrito, db_column='UBIGEO')
    zona = models.CharField(db_column='ZONA', max_length=10, blank=True, null=True)
    idmanzana = models.CharField(db_column='IDMANZANA', max_length=20, blank=True, null=True)
    aeu = models.IntegerField(db_column='AEU', blank=True, null=True)
    viv_aeu = models.IntegerField(db_column='VIV_AEU', blank=True, null=True)

    def __unicode__(self):
        return '%s , %s' % (self.ubigeo, self.zona)

    class Meta:
        managed = False
        db_table = 'MZS_AEU'
