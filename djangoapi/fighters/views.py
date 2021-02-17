from rest_framework.viewsets import ModelViewSet
from fighters.models import Fighter
from .serializers import FighterSerializer

# CRUD OPERATIONS defined. Define how to to covert json to python (serializer we made), and which objects to query
 
class FightersViewSet(ModelViewSet): #magic is in inheriting ModelView Sub class
    queryset = Fighter.objects.all() #specify the data, queryset
    serializer_class = FighterSerializer

# don't modify request data here, do it in serializer