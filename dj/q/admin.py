from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

																																																							 
from django.db import models																																																												  
from django.forms import CheckboxSelectMultiple  
from django.contrib.admin.views.main import ChangeList

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
	readonly_fields = ('partner',)
	def save_model(self, request, obj, form, change):
		obj.partner = Partner.objects.get(user=request.user)
		super().save_model(request, obj, form, change)
	def get_queryset(self, request):
		p = Partner.objects.get(user=request.user)
		qs = super().get_queryset(request)
		return qs.filter(partner = p)

class Order2(Order):
	class Meta:
		proxy = True
		verbose_name = 'Прибыль'
		verbose_name_plural = 'Прибыль'
class IncomeAdmin(admin.ModelAdmin):
	list_filter = (
		('date', DateFieldListFilter),
	)
	def changelist_view(self, request, extra_context=None):
		response = super().changelist_view(request, extra_context)
		filtered_query_set = response.context_data["cl"].queryset
		response.context_data["cl"].result_count = self.get_some_data(filtered_query_set)
		return response
	def get_some_data(self, qs):
		s = 0
		for q in qs:
			try:
				s += int(q.quest.price)
			except:
				pass
		print(s)
		return s
class OrderAdmin(admin.ModelAdmin):
	list_filter = (
		('date', DateFieldListFilter),
	)


admin.site.register(Partner)
admin.site.register(Client)
admin.site.register(Quest2, QuestForPartner)
admin.site.register(Quest, QuestAdmin)
admin.site.register(Review)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order2, IncomeAdmin)
admin.site.register(TimeSlot)
admin.site.register(City)
admin.site.register(Discount)
#p0o9i8u7y6