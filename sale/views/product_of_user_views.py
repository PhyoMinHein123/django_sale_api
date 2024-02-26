from .imports import *
# Create your views here.

@api_view(['GET'])
# @permission_required('my_store.view_datasmodel', raise_exception=True)
@authentication_classes([TokenAuthentication])
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
@authentication_classes([TokenAuthentication])
def POUStore(request):
    seri = ProductOfUserSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def POUShow(request, pk):
    try:
        datas = ProductOfUser.objects.get(pk=pk)
        seri = ProductOfUserSerializer(datas)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
def POUUpdate(request, pk):
    try:
        datas = ProductOfUser.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    seri = ProductOfUserSerializer(datas, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def POUDelete(request, pk):
    try:
        datas = ProductOfUser.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    datas.delete()
    return Response({"message":"Deleted Successfully"},status=200)