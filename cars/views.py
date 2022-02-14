from importlib.util import resolve_name
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def cars_list(request):



    return Response('ok')