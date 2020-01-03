from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, DeleteView

from .models import Item


# Create your views here.

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    fields = '__all__'
    def get_success_url(self):
        return reverse('home')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    
def home(request):
    items = Item.objects.all()
    print(Item)
    return render(request, 'home.html', { 'items' : items })


