from django.contrib import admin
from .models import Mehandi, Category, Payment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


class MehandiAdmin(admin.ModelAdmin):
    list_display = ('id', 'mehandi_name', 'price',
                    'description', 'image', 'category')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_no', 'cvv', 'expiry_date', 'balance')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Mehandi, MehandiAdmin)
admin.site.register(Payment, PaymentAdmin)
