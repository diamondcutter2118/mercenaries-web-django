from django.contrib import admin
from .models import User,Offer,Game
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","email","password")

class OfferAdmin(admin.ModelAdmin):
    list_display = ("id","game","required_time","required_rank","reward_ingame","salary","description")

class GameAdmin(admin.ModelAdmin):
    list_display = ("id","offer")


admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Game)