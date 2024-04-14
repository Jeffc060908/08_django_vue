from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.views import View
from django.shortcuts import get_object_or_404
from .models import grocery_list, grocery



# Create your views here.

class GroceryListView(ListView):
    model = grocery
    
class GroceryCreateView(CreateView):
    model = grocery 
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Actor "{grocery_name}" has been created'.format(
                grocery_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("groceries:grocery_detail", args=[self.object.id])

class GroceryDetailView(DetailView):
    model = grocery
    
class GroceryUpdateView(UpdateView):
    model = grocery
    fields = ['name']
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Actor "{grocery_name}" has been updated'.format(
                grocery_name=self.object.name))
        return response
    
    def get_success_url(self):
        return reverse_lazy("groceries:grocery_detail", args=[self.object.id])


class GroceryDeleteView(DeleteView):
    model = grocery
    success_url = reverse_lazy("groceries:grocery_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Actor "{grocery_name}" has been deleted'.format(
                grocery_name=self.object.name))
        return response