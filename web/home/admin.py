from django.contrib import admin
from .models import User,Offer,Game,Tag
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","email","password")

class OfferAdmin(admin.ModelAdmin):
    list_display = ("id","game","user","required_time","required_rank","reward_ingame","number_of_recruit_player","salary","description")

class GameAdmin(admin.ModelAdmin):
    list_display = ("id","name","offer","category","description","tag")

class TagAdmin(admin.ModelAdmin):
    list_display = ("name")


admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Game)
admin.site.register(Tag)