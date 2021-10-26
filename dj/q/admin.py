from django.contrib import admin

                                                                                                                                                                                                                             
from django.db import models                                                                                                                                                                                                                                                  
from django.forms import CheckboxSelectMultiple  

from .models import Partner, Client, Quest, Order, Review, TimeSlot


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Partner)
admin.site.register(Client)
admin.site.register(Quest, MyModelAdmin)
admin.site.register(Review)
admin.site.register(Order)                                                                                                                                                                                                                                
admin.site.register(TimeSlot)    
