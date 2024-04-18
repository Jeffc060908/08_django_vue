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
from .models import GList, Grocery
from .forms import ListForm
import simplejson as json



# Create your views here.

#################################### GROCERIES #################################

class GroceryListView(LoginRequiredMixin, ListView):
    model = Grocery
    
class GroceryCreateView(CreateView):
    model = Grocery 
    fields = ['name', 'price']
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Grocery "{grocery_name}" has been created'.format(
                grocery_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("groceries:grocery_detail", args=[self.object.id])

class GroceryDetailView(DetailView):
    model = Grocery
    
class GroceryUpdateView(UpdateView):
    model = Grocery
    fields = ['name', 'price']
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
    model = Grocery
    success_url = reverse_lazy("groceries:grocery_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Grocery "{grocery_name}" has been deleted'.format(
                grocery_name=self.object.name))
        return response


########################################### LISTS ######################################

class ListListView(LoginRequiredMixin, ListView):
    model = GList
    
class ListDetailView(DetailView):
    model = GList
    
class ListCreateView(CreateView):
    model = GList
    form_class = ListForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'List "{list_name}" has been created'.format(
                list_name=self.object.name))
        return response

    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("groceries:list_detail", args=[self.object.id])
        # you can also use it this way with kwargs, just to let you know
        # but here we have only one argument, so no mistake can be done
        #return reverse_lazy("movies:actor_detail",
        #                    kwargs={'pk':self.object.id})
        
class ListDeleteView(DeleteView):
    model = GList
    success_url = reverse_lazy("groceries:glist_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Grocery List "{list_name}" has been deleted'.format(
                list_name=self.object.name))
        return response
    
class ListUpdateView(UpdateView):
   model = GList

   fields = ['date_of_creation', 'groceries', 'name']

   def form_valid(self, form):
       response = super().form_valid(form)
       messages.add_message(
           self.request,
           messages.SUCCESS,
           'List "{list_name}" has been updated'.format(
               list_name=self.object.name
           ),
       )
       return response

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       
       glist_dico = model_to_dict(self.object)
       glist_dico["date_of_creation"] = glist_dico["date_of_creation"].strftime(
           "%Y-%m-%d"
       )
       groceries = glist_dico["groceries"]
       glist_grocery_list = []
       for grocery in groceries:
           glist_grocery_list.append({"name": grocery.name, "price": grocery.price})
       glist_dico["groceries"] = json.dumps(glist_grocery_list)
       grocery_list = list(Grocery.objects.all().values())
       context["glist_dict"] = json.dumps(glist_dico)
       context["grocery_list"] = json.dumps(grocery_list)
       print("context", context)
       return context

   # comment the following line to show the error about not having an
   # success_url
   def get_success_url(self):
       return reverse_lazy("groceries:list_detail", args=[self.object.id])
       