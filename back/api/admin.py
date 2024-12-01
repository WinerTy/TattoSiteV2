from django.contrib import admin

from .models import Salon, SalonSocialNetwork, Master, Slider, Tags


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


@admin.register(Master)
class AdminMaster(admin.ModelAdmin):
    list_display = ("name", "phone", "salon")
    list_filter = ("salon",)
    search_fields = ("name", "salon__name")
    ordering = ("name", "phone", "salon")


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("image", "description")
    search_fields = ("image", "description")
    list_filter = ("image", "description")
    ordering = ("image", "description")


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)
