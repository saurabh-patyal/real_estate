from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display=('id' , 'title','is_published','price','list_date','realtor')
    list_display_links=('id','title')
    list_editable=('is_published',)
    list_filter=('title','list_date','city')
    list_per_page=20
    search_fields=('city','title','realtor')




admin.site.register(Listing,ListingAdmin)