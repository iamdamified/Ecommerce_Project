from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Hero)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price"]
admin.site.register(Social)
admin.site.register(Subscriber)





# class ContactAdmin(admin.ModelAdmin):
#     list_display = ["name", "subject", "message"]

# admin.site.register(Contact, ContactAdmin)


# class ContactinfoAdmin(admin.ModelAdmin):
#     list_display = ["name", "email", "message"]

# admin.site.register(Contactinfo, ContactinfoAdmin) # This could be used and the above deleted
