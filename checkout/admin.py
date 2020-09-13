from django.contrib import admin

from .models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdmin,)

    readonly_fields = (
        'order_id', 
        'date',
        'total',
        'shopping_cart',
        'stripe_pid'
    )

    fields = (
        'order_id',
        'user_profile',
        'date',
        'total',
        'shopping_cart',
        'stripe_pid'
    )

    list_display = (
        'order_id',
        'date',
        'total'
    )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
