from django.urls import path
from . import views

# to be converted to a loop function #

app_name = 'offers'
urlpatterns =[
    path ("offer1", views.offer1, name ="offer1" ),
    path ("offer2", views.offer2, name ="offer2" ),
    path ("offer3", views.offer3, name ="offer3" )
]