from django.contrib import admin

from .models import Partner, Client, Quest, Order, Review

admin.site.register(Partner)
admin.site.register(Client)
admin.site.register(Quest)
admin.site.register(Review)
admin.site.register(Order)

# Register your models here.
