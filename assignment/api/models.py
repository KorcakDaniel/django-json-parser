from django.db import models


class AttributeName(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    display = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class Attribute(models.Model):
    attribute_name = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return self.attribute_name.name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="CZK", blank=True)
    published_on = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductAttributes(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.URLField()

    def __str__(self):
        return self.image


class ProductImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Catalog(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    attributes = models.ManyToManyField(Attribute, blank=True)

    def __str__(self):
        return self.name
