from django.db import models

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    username = models.CharField(max_length = 10)
    email = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    confirm_password = models.CharField(max_length = 20,null = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    
    name = models.CharField(max_length=30, null=True)
    category = models.CharField (max_length = 30, null =True)
    description = models.CharField (max_length = 1000, null = True)
    tags = models.ManyToManyField(Tag, blank = True, related_name ="Tag" )
    def __str__(self):
        return self.name

class Offer (models.Model):
    STATUS =(
    ('Open','Open'),
    ('Closed','Closed')
    )
    id = models.BigAutoField(primary_key=True)
    # insert related name of the game
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name = "game_name", null = True)
    # insert related name of the user
    created_by = models.CharField(max_length= 30,null = True)
    required_time = models.CharField(max_length = 100)
    required_rank = models.CharField(max_length = 100)
    reward_ingame = models.CharField(max_length = 100)
    number_of_recruit_player =models.IntegerField(null = True)
    salary = models.CharField(max_length = 100)
    description =models.CharField(max_length = 1000)
    def __str__(self):
        return f"Offer {self.id} : {self.game}"
       

