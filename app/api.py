from rest_framework import permissions
from rest_framework import routers, serializers, viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Product



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductListAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    model = serializer_class.Meta.model
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]


    # def get_queryset(self):
    #     barcode = self.kwargs.get('barcode')
    #     print(self.kwargs)
    #     queryset = self.model.objects.filter(barcode=barcode)
    #     return queryset

router = routers.DefaultRouter()
router.register('product', ProductListAPIView, basename='Product')



def filter_product(request):
    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method not Allowed', 
            'status_code': 405
        }, status=405)
    
    barcode = request.POST.get('barcode')
    products = Product.objects.filter(barcode__icontains=barcode)

    data = {'data': list(products.values())}
    return JsonResponse(data)