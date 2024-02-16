from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

import api.helpers as helpers


@api_view(["POST"])
@parser_classes([JSONParser])
def import_data(request):
    errors, data = helpers.import_data(request)
    return Response({"received data": data, "errors": errors})


@api_view(["GET"])
def get_model(_, model_name):
    serializer = helpers.get_model(model_name)
    return Response({"message": serializer.data})


@api_view(["GET"])
def get_entry(_, model_name, id):
    serializer = helpers.get_entry(model_name, id)
    return Response({"message": serializer.data})
