from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    password = models.CharField(max_length=10, verbose_name='Password')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y %H:%M:%S')

    def get_updated_at(self):
        return self.update_at.strftime('%d/%m/%Y %H:%M:%S')


class Products(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')
    price = models.DecimalField(max_digits=13, decimal_places=2, verbose_name='Price')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y %H:%M:%S')

    def get_updated_at(self):
        return self.update_at.strftime('%d/%m/%Y %H:%M:%S')


class Orders(models.Model):
    customer_id = models.ForeignKey('Customers', on_delete=models.DO_NOTHING, verbose_name='Customers ID')
    produtcts_id = models.ForeignKey('Products', on_delete=models.DO_NOTHING, related_name='produtos', verbose_name='Products ID')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{str(self.customer_id)} - {str(self.produtcts_id)}'

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y %H:%M:%S')

    def get_updated_at(self):
        return self.update_at.strftime('%d/%m/%Y %H:%M:%S')



