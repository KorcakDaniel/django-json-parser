from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
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


@api_view(["POST"])
@parser_classes([JSONParser])
def importData(request):
    errors = []
    data = []
    for item in request.data:
        model_name = list(item.keys())[0]

        try:
            model = apps.get_model("api", model_name)
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

    return Response({"received data": data, "errors": errors})


@api_view(["GET"])
def getModel(_, model_name):
    try:
        model = apps.get_model("api", model_name)
    except LookupError:
        raise Http404(f"{model_name} is not a valid model.")
    queryset = model.objects.all()
    serializer_ref = globals().get(f"{model_name}Serializer")
    serializer = serializer_ref(queryset, many=True)
    return Response({"message": serializer.data})


@api_view(["GET"])
def getEntry(_, model_name, id):
    try:
        model = apps.get_model("api", model_name)
    except LookupError:
        raise Http404(f"{model_name} is not a valid model.")
    queryset = get_list_or_404(model, id=id)
    serializer_ref = globals().get(f"{model_name}Serializer")
    serializer = serializer_ref(queryset, many=True)
    return Response({"message": serializer.data})
