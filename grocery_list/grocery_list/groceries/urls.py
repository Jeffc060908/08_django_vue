from django.urls import path

from . import views


app_name = "groceries"

urlpatterns = [
        path("groceries/", views.GroceryListView.as_view(), name="grocery_list"),
        path("groceries/<int:pk>", views.GroceryDetailView.as_view(), name="grocery_detail"),
        path("groceries/new", views.GroceryCreateView.as_view(), name="grocery_create"),
        path("groceries/update/<int:pk>", views.GroceryUpdateView.as_view(),
             name="grocery_update"),
        path("groceries/delete/<int:pk>", views.GroceryDeleteView.as_view(),
         name="grocery_delete"),
        path("lists/", views.ListListView.as_view(), name="glist_list"),
        path("lists/new", views.ListCreateView.as_view(), name="list_create"),
        path("lists/<int:pk>", views.ListDetailView.as_view(),
         name="list_detail"),
        path("lists/update/<int:pk>", views.ListUpdateView.as_view(),
         name="glist_update"),
        path("lists/delete/<int:pk>", views.ListDeleteView.as_view(),
         name="glist_delete"),



]