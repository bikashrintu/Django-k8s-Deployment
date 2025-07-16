from django.urls import path
from . import views
 

urlpatterns=[
  path("",views.home,name='home'),
  path("review/",views.review,name='review'),
  path("car/<int:car_id>/",views.product_details,name="product_details"),
  # path('reviews/',views.display_reviews, name='display_reviews'),  # New page for reviews
 ]