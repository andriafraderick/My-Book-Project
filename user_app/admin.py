from django.contrib import admin
from .models import LoginTable, UserProfile, Cart, CartItem

admin.site.register(UserProfile)
admin.site.register(LoginTable)
admin.site.register(Cart)
admin.site.register(CartItem)
