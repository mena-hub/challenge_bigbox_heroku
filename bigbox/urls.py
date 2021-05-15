from django.urls import path
from bigbox import views

bigbox_patterns = ([
    path('', views.boxes, name="boxes"),
    path('<int:box_id>/', views.box_detail, name="box_detail"),
    path('<int:box_id>/activity/', views.activities, name="activities"),
    path('<int:box_id>/activity/<int:activity_id>', views.activity_detail, name="activity_detail"),
    path('<slug:slug>/', views.box_detail_tag, name="tag"),
], 'bigbox')