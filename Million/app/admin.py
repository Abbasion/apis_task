from django.contrib import admin

from .models import Stock, InsiderTransaction, Valuation

# Register your models here.
admin.site.register(Stock)
admin.site.register(InsiderTransaction)
admin.site.register(Valuation)