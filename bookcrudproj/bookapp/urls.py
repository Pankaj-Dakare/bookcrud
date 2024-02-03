from bookapp import views
from django.urls import path

urlpatterns = [
   path("homepage",views.homepage),
   path("addbook",views.addbook),
   path('delete/<bookid>',views.delete),
   path('update/<bookid>',views.update)
]