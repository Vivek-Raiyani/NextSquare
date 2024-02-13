from django.contrib import admin
from .models import Properties, Persons, Reviews, Wishlist, Rentals, Payments

# Register your models here.
admin.site.register(Properties)
admin.site.register(Persons)
admin.site.register(Reviews)
admin.site.register(Wishlist)
admin.site.register(Rentals)
admin.site.register(Payments)
