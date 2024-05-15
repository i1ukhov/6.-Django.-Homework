from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}) написал: {message}')
#     return render(request, 'catalog/contacts.html')

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'{name} ({phone}) написал: {message}')
        return HttpResponseRedirect(self.request.path)
