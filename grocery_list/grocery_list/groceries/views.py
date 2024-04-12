from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict

from .models import Grocery, List
from .forms import ListForm
from django.views import View

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.

class GroceryListView(ListView):
    model = Grocery

class GroceryCreateView(CreateView):
    model = Grocery
    fields = ['name']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Grocery "{grocery_name}" has been created'.format(
                grocery_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("groceries:grocery_detail", args=[self.object.id])