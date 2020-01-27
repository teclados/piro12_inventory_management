from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView

from management.forms import ItemForm, ClientForm
from management.models import Item, Client


def item_list(request):
    items = Item.objects.all()
    return render(request, 'management/item_list.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'management/item_detail.html', {
        'item': item,
    })


item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)


def item_delete(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == 'GET':
        return redirect('management:item_detail', item.id)
    elif request.method == 'POST':
        item.delete()
        return redirect('management:item_list')


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'management/client_list.html', {'clients': clients})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'management/client_detail.html', {
        'client': client,
    })


client_new = CreateView.as_view(model=Client, form_class=ClientForm)
client_edit = UpdateView.as_view(model=Client, form_class=ClientForm)


def client_delete(request, pk):
    client = Client.objects.get(pk=pk)

    if request.method == 'GET':
        return redirect('management:client_detail', client.id)
    elif request.method == 'POST':
        client.delete()
        return redirect('management:client_list')


def button_down(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.quantity != 0:
        item.quantity -= 1
    item.save()
    return redirect('management:item_list')


def button_up(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.quantity += 1
    item.save()
    return redirect('management:item_list')