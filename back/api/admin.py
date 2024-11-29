from django.contrib import admin

from .models import Salon, SalonSocialNetwork


class SocialNetworkInline(admin.TabularInline):
    model = SalonSocialNetwork
    extra = 1


@admin.register(Salon)
class AdminSalon(admin.ModelAdmin):
    list_display = ("name", "address", "longitude", "latitude")
    search_fields = ("name", "address", "longitude", "latitude")
    list_filter = ("name", "address", "longitude", "latitude")
    ordering = ("name", "address", "longitude", "latitude")
    inlines = [SocialNetworkInline]
