from .imports import *
# Create your views here.

@api_view(['GET'])
# @permission_required('my_store.view_datasmodel', raise_exception=True)
@authentication_classes([TokenAuthentication])
def TransactionIndex(request):
    try:
        datas = Transaction.objects.all()
        paginator = CustomPagination()
        page_obj = paginator.paginate_queryset(datas, request)
        seri = TransactionSerializer(page_obj, many=True)
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":str(e)}, status=500)
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def TransactionStore(request):
    seri = TransactionSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def TransactionShow(request, pk):
    try:
        datas = Transaction.objects.get(pk=pk)
        seri = TransactionSerializer(datas)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
def TransactionUpdate(request, pk):
    try:
        datas = Transaction.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    seri = TransactionSerializer(datas, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def TransactionDelete(request, pk):
    try:
        datas = Transaction.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    datas.delete()
    return Response({"message":"Deleted Successfully"},status=200)