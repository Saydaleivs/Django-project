from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    id = request.GET.get('id', None) or None

    if id is not None:
        isExistUser = Item.objects.filter(id=id).exists()

        if isExistUser is False:
            return Response('User is not exist')

        item = Item.objects.get(id=id)
        serializer = ItemSerializer(item)

        return Response(serializer.data)

    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateData(request):
    id = request.GET.get('id', None) or None

    if id is None:
        return Response('id parameter is required')

    isAvailableUser = Item.objects.filter(id=id).exists()

    if isAvailableUser is False:
        return Response('User is not exist')

    user = Item.objects.get(id=id)
    serializer = ItemSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request):
    id = request.GET.get('id', None)

    serializer = Item.objects.filter(id=id)
    serializer.delete()

    return Response('Deleted successfully')
