from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics,status

#1-usul class yordamida keng qo'llanadaigan usul
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books ",
            'books': serializer_data
        }
        return Response(data)


# class BookDetailApiView(generics.RetrieveAPIView):
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer

class BookDetailApiView(APIView):


    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                'status': 'successful',
                'book': serializer_data
            }
            return Response(data)

        except Exception:
            data ={
                'status': 'Does not exists',
                'message': 'book not found'
            }
            return Response(data)


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        book.delete()
        return Response({
                "status": True,
                "Message": "Succesfully deleted"
            })
        # try:
        #     book = Book.objects.get(id=pk)
        #     book.delete()
        #     return Response({
        #         "status": True,
        #         "Message": "Succesfully deleted"
        #     }, status.HTTP_200_OK)
        # except Exception:
        #     return Response(
        #         {
        #             "status": False,
        #             "Message": "Book is not found"
        #         }, status.HTTP_400_BAD_REQUEST
        #     )


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": 'Book saved to the database',
                'books': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#viewset yordamida crud->create, read,update,delete urllarini bir viewda yozish
class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 2-usul function view in DRF funksiya yordamida kam ishlatiladi deyarli ishlatilmaydi
# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     seralizer = BookSerializer(books, many=True)
#     return Response(seralizer.data)



