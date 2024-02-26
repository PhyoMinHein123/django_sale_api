from .imports import *
# Create your views here.

@api_view(['GET'])
# @permission_required('my_store.view_productsmodel', raise_exception=True)
@authentication_classes([TokenAuthentication])
def ProductIndex(request):
    try:
        products = Product.objects.all()
        paginator = CustomPagination()
        page_obj = paginator.paginate_queryset(products, request)
        seri = ProductSerializer(page_obj, many=True)
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":str(e)}, status=500)
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def ProductStore(request):
    seri = ProductSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def ProductShow(request, pk):
    try:
        products = Product.objects.get(pk=pk)
        seri = ProductSerializer(products)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"errors":"product Not Found!"}, status=204)
    
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
def ProductUpdate(request, pk):
    try:
        products = Product.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"product Not Found!"}, status=204)
    seri = ProductSerializer(products, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def ProductDelete(request, pk):
    try:
        products = Product.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"product Not Found!"}, status=204)
    products.delete()
    return Response({"message":"Deleted Successfully"},status=200)