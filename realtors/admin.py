from realtors.models import Realtor
from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','email','is_mvp','hire_date')
    list_display_links=('id','name')
    list_editable=('is_mvp',)
    list_filter=('name','hire_date','email')
    list_per_page=20
    search_fields=('email','name')



admin.site.register(Realtor,RealtorAdmin)