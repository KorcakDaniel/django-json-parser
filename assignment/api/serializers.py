from rest_framework import serializers
from .models import (
    Attribute,
    AttributeName,
    AttributeValue,
    Product,
    ProductAttributes,
    Image,
    ProductImage,
    Catalog,
)

"""Had a source argument with PrimaryKeyRelatedFields and so on, to map it
to the unified model structure, but decided that unifying the input would be
better and probably desired."""


class AttributeNameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = AttributeName
        fields = ("id", "name", "code", "display")


class AttributeValueSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = AttributeValue
        fields = ("id", "value")


class AttributeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Attribute
        fields = ("id", "attribute_name", "attribute_value")


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "currency",
            "published_on",
            "is_published",
        )


class ProductAttributesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ProductAttributes
        fields = ("id", "attribute", "product")


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Image
        fields = ("id", "name", "image")


class ProductImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ProductImage
        fields = ("id", "name", "image", "product")


class CatalogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Catalog
        fields = ("id", "name", "image", "products", "attributes")
