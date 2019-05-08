
from django import template


register = template.Library()

@register.simple_tag
def cek_harga(**kwargs):
    cart = kwargs.get('jumlah')
    total_harga = int(cart) * 1000 
    return total_harga