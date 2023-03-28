# from django.shortcuts import render
# from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import viewsets
# from rest_framework.decorators import action


from .models import Women
from .serializers import WomenSerializer
from .permissions import (
    IsAdminOrReadOnly,
)


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)


# Create your views here.

# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()[:3]
#     serializer_class = WomenSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')

#         if not pk:
#             return Women.objects.all().select_related('cat')[:3]

#         return Women.objects.filter(pk=pk).select_related('cat')

#     @action(methods=['get'], detail=False)
#     def categorys(self, request):
#         cats = Category.objects.all()
#         return(Response({'category' : [c.name for c in cats]}))


#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return(Response({'category' : cats.name}))


# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'post' : WomenSerializer(w, many=True).data})


#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()
#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)

#         if not pk:
#             return Response({'error' : 'method put is not allowed'})

#         try:
#             instanse = Women.objects.get(pk=pk)
#         except:
#             return Response({'error' : 'object does not exists'})

#         serializer = WomenSerializer(data=request.data, instance=instanse)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post' : serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)

#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({'error' : 'object does not exists'})

#         if not pk:
#             return Response({'error' : 'method delete is not allowed'})


#         return Response({'delete' : 'delete post'+str(pk)})


# # class WomenAPIView(generics.ListAPIView):
# #     queryset = Women.objects.all()
# #     serializer_class = WomenSerializer
