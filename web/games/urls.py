from django.urls import path
from . import views

app_name = 'games'
urlpatterns =[
    path ("decentraland",views.decentraland, name ="decentraland" ),
    path ("axieinfinity",views.axieinfinity, name ="axieinfinity" ),
    path ("alienworld", views.alienworld, name ="alienworld" )
]
