from django.db import models

# Create your models here.

class Offer (models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.CharField(max_length=30)
    required_time = models.CharField(max_length = 100)
    required_rank = models.CharField(max_length = 100)
    reward_ingame = models.CharField(max_length = 100)
    salary = models.CharField(max_length = 100)
    description =models.CharField(max_length = 1000)

    def __str__(self):
        return f"Offer {self.id} : {self.game}"

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    username = models.CharField(max_length = 10)
    email = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    offers = models.ForeignKey(Offer, blank =True, on_delete=models.CASCADE, related_name ="Requirement",null =True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 

class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    offer = models.ForeignKey(Offer, blank =True, on_delete=models.CASCADE, related_name ="User_posts",null =True)


       

