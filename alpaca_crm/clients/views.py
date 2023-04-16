from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from django.urls import reverse_lazy
from .forms import CustomerForm
# Create your views here.


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'client_list.html'
    context_object_name = 'customers'

    login_url = reverse_lazy('home')

class CustomerCreate(CreateView):
    
    template_name = 'client_add.html'
    form_class = CustomerForm
    success_url = reverse_lazy('list_clients')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class CustomerDetails(DetailView):
    model = Customer
    template_name = 'client_details.html'
    context_object_name = 'customer'


class CustomerUpdate(UpdateView):
    model = Customer
    template_name = 'client_edit.html'
    form_class = CustomerForm
    context_object_name = "customer"

    def get_success_url(self) -> str:
        customer_id = self.object.id
        return reverse_lazy('detail_client', kwargs={'pk': customer_id})


class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'client_delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('list_clients')