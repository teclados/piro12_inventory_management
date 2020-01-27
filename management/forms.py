from django import forms
from .models import Item, Client


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
