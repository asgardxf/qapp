from django.contrib import admin

                                                                                                                                                                                                                             
from django.db import models                                                                                                                                                                                                                                                  
from django.forms import CheckboxSelectMultiple  

from .models import Partner, Client, Quest, Order, Review, TimeSlot, PhotoAux, Discount, City

class inLinePhoto(admin.StackedInline):
	model = PhotoAux

class QuestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    inlines = [inLinePhoto]


class Quest2(Quest):
	class Meta:
		proxy = True
		verbose_name = 'Квест партнёра'
		verbose_name_plural = 'Квесты партнёра'
class QuestForPartner(QuestAdmin):
	def get_queryset(self, request):
		p = Partner.objects.get(user=request.user)
		qs = super().get_queryset(request)
		return qs.filter(partner = p)


admin.site.register(Partner)
admin.site.register(Client)
admin.site.register(Quest2, QuestForPartner)
admin.site.register(Quest, QuestAdmin)
admin.site.register(Review)
admin.site.register(Order)                                                                                                                                                                                                                                
admin.site.register(TimeSlot)
admin.site.register(City)
admin.site.register(Discount)
#p0o9i8u7y6