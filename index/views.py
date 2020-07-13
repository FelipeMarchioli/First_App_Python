from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer
from .models import Book
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist

#Welcome
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)

#API that returns the list of all books
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_books(request, headquarter):
    books = Book.objects.filter(headquarter=headquarter, deleted=False)
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)

#API that insert a new book of a specific headquarter
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_book(request):
    payload = json.loads(request.body)
    try:
        book = Book.objects.create(
            title=payload["title"],
            image=payload["image"],
            headquarter=payload["headquarter"],
            author=payload["author"],
            pages=payload["pages"],
            deleted=False
        )
        serializer = BookSerializer(book)
        return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#API that will update a book
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_book(request):
    payload = json.loads(request.body)
    try:
        book = Book.objects.update(
            id=payload["id"],
            title=payload["title"],
            image=payload["image"],
            headquarter=payload["headquarter"],
            author=payload["author"],
            pages=payload["pages"],
            deleted=False,
            created_date=payload["created_date"]
        )
        serializer = BookSerializer(book)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#API that will delete a book logically
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_book(request):
    payload = json.loads(request.body)
    try:
        payload["deleted"] = True
        book_item = Book.objects.update(**payload)
        book = Book.objects.get(id=payload["id"])
        serializer = BookSerializer(book)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)