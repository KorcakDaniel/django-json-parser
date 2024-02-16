from django.http import Http404
from django.shortcuts import get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from django.apps import apps

from .serializers import (
    AttributeSerializer,
    AttributeNameSerializer,
    AttributeValueSerializer,
    ProductSerializer,
    ProductAttributesSerializer,
    ImageSerializer,
    ProductImageSerializer,
    CatalogSerializer,
)


def import_data(request):
    errors = []
    data = []
    for item in request.data:
        try:
            model_name = list(item.keys())[0]
            model = apps.get_model("api", model_name)
        except AttributeError:
            ValidationError.status_code = 422
            raise ValidationError({"message": "Please provide a valid JSON object."})
        except LookupError:
            return Response({"message": f"{model_name} is not a valid model."})

        serializer_ref = globals().get(f"{model_name}Serializer")
        id = item[model_name].get("id")

        try:
            existing_instance = model.objects.get(id=id)
            serializer = serializer_ref(
                instance=existing_instance, data=item[model_name]
            )
        except ObjectDoesNotExist:
            serializer = serializer_ref(data=item[model_name])

        if serializer.is_valid():
            serializer.save()
            data.append(serializer.data)
        else:
            errors.append({"error": f"{model_name} - {serializer.errors}"})
    return errors, data


def get_model(model_name):
    try:
        model = apps.get_model("api", model_name)
    except LookupError:
        raise Http404(f"{model_name} is not a valid model.")
    queryset = model.objects.all()
    serializer_ref = globals().get(f"{model_name}Serializer")
    return serializer_ref(queryset, many=True)


def get_entry(model_name, id):
    try:
        model = apps.get_model("api", model_name)
    except LookupError:
        raise Http404(f"{model_name} is not a valid model.")
    queryset = get_list_or_404(model, id=id)
    serializer_ref = globals().get(f"{model_name}Serializer")
    return serializer_ref(queryset, many=True)
