from django.contrib import admin
from .models import Customer,Offer,Game,Tag
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","username","email","password","profile_pic")

class OfferAdmin(admin.ModelAdmin):
    list_display = ("id","game","user","required_time","required_rank","reward_ingame","number_of_recruit_player","salary","description")

class GameAdmin(admin.ModelAdmin):
    list_display = ("id","name","offer","category","description","tag")

class TagAdmin(admin.ModelAdmin):
    list_display = ("name")


admin.site.register(Customer)
admin.site.register(Offer)
admin.site.register(Game)
admin.site.register(Tag)