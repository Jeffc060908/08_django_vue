from django.urls import path

from . import views


app_name = "groceries"

urlpatterns = [
        path("groceries/", views.GroceryListView.as_view(), name="grocery_list"),
        path("groceries/<int:pk>", views.GroceryDetailView.as_view(), name="grocery_detail"),
        path("groceries/new", views.GroceryCreateView.as_view(), name="grocery_create"),



]
