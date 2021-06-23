from django.contrib import admin
from .models import Contact
# Register your models here.

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','contact_date')
    list_display_links=('name','email')
    list_per_page=20
    search_fields=('name','email','phone','contact_date')




admin.site.register(Contact,ContactAdmin)
