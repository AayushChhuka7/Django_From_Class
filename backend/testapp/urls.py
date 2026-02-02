
from django.urls import path
from . import views

#yei hunu parxha 
urlpatterns = [
    #'' yo bhaneko / ma 
    path('',views.index),
    # path('january/',views.january),
    # path('february/',views.february),
    # path('march/',views.march),


    ##dynamic
    path('<int:month>/',views.monthlychallange_by_num,name='monthly-challange-by-num'),
    path('<str:month>/',views.monthlychallange,name='monthly-challange'),

]