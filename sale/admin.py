from django.contrib import admin
from sale.models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOfUser)
admin.site.register(Transaction)
admin.site.register(Request)