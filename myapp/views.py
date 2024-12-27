from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer  # We will create this serializer next

# GET View (Already there)
@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    data = [{"id": item.id, "name": item.name} for item in items]
    return Response(data)

# POST View for creating new Item
@api_view(['POST'])
def create_item(request):
    if request.method == 'POST':
        # Use the ItemSerializer to validate and save data
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
