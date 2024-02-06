from django.contrib import admin
from .models import (
    AttributeName,
    AttributeValue,
    Attribute,
    Product,
    ProductAttributes,
    Image,
    Catalog,
)

admin.site.register(AttributeName)
admin.site.register(AttributeValue)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAttributes)
admin.site.register(Image)
admin.site.register(Catalog)
