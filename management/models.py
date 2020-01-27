from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='이름')
    phone = models.CharField(max_length=20, verbose_name='전화번호')
    address = models.CharField(max_length=30, verbose_name='주소')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('management:client_detail', args=[self.pk])


class Item(models.Model):
    name = models.CharField(max_length=20, verbose_name='제품명')
    photo = models.ImageField(null=True, blank=True, upload_to='images', verbose_name='제품 사진')
    content = models.TextField(null=True, blank=True, verbose_name='제품 설명')
    price = models.PositiveIntegerField(verbose_name='가격')
    quantity = models.PositiveIntegerField(verbose_name='남은 수량')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='거래처', related_name='item')

    def get_absolute_url(self):
        return reverse('management:item_detail', args=[self.pk])
