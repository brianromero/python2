from django.contrib import admin
from .models import Manzana_seg


# Register your models here.
# admin.site.register(Product)
@admin.register(Manzana_seg)
class AdminProduct(admin.ModelAdmin):
    list_display = ('ubigeo', 'zona', 'aeu_seccion', 'aeu', 'aeu_viv')
    list_filter = ('zona',)
