from .imports import *
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def POUIndex(request):
    try:
        datas = ProductOfUser.objects.all()
        paginator = CustomPagination()
        page_obj = paginator.paginate_queryset(datas, request)
        seri = ProductOfUserSerializer(page_obj, many=True)
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":str(e)}, status=500)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def POUStore(request):
    seri = ProductOfUserSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def POUShow(request, pk):
    try:
        datas = ProductOfUser.objects.get(pk=pk)
        seri = ProductOfUserSerializer(datas)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def POUUpdate(request, pk):
    try:
        datas = ProductOfUser.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    seri = ProductOfUserSerializer(datas, data=request.data, partial=True)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def POUDelete(request, pk):
    try:
        datas = ProductOfUser.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    datas.delete()
    return Response({"message":"Deleted Successfully"},status=200)