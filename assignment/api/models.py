from django.db import models


class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255)
    kod = models.CharField(max_length=255, blank=True, null=True)
    zobrazit = models.BooleanField(default=False)

    def __str__(self):
        return self.nazev


class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    hodnota = models.CharField(max_length=255)

    def __str__(self):
        return self.hodnota


class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev_atributu = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255)
    description = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    mena = models.CharField(max_length=3)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField()


class ProductAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    obrazek = models.URLField()


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=255)


class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    products_ids = models.JSONField()
    attributes_ids = models.JSONField()
