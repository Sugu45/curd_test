from django.db.models import Q
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import json
from .models import *
from .core_serlizer import author_serlizer,book_serlizer
# Create your views here.
@api_view(['GET','POST'])
def author_create(request):
    try:
        data=json.loads(request.body)
        if 'id' in data:
            author_id = data.pop('id')
            author_update=Author.objects.filter(id=author_id).update(**data)
            if author_update:
                author_data = Author.objects.get(id=author_id)
                author_serlizer_data=author_serlizer(author_data).data
                return JsonResponse(author_serlizer_data,safe=False)
            else:
                return JsonResponse("Updation Failed")
        else:
            author_create = Author.objects.create(**data)
            if author_create:
                author_serlizer_data = author_serlizer(author_create).data
                return JsonResponse(author_serlizer_data, safe=False)
            else:
                return JsonResponse("Creation Failed")
    except Exception as exe:
        res = {'error': exe}
        return JsonResponse(res, safe=False)

@api_view(['POST'])
def author_get(request):
    try:
        data = json.loads(request.body)
        conditions=Q()
        if 'name' in data and 'name' !="":
            conditions&=Q(name__icontains=data.get('name'))
        current_page=request.POST.get('page',1)
        page_size=request.POST.get('page_size',10)
        offset=(current_page-1)*page_size
        author_data=Author.objects.filter(conditions)[offset:offset+page_size]
        author_ser=author_serlizer(author_data,many=True).data
        user_data_count = Author.objects.filter(conditions).count()
        total_pages = (user_data_count+page_size-1)//page_size
        has_next = current_page < total_pages
        has_pervious = current_page > 1
        data = {"data": author_ser,
                'page_number': current_page,
                'page_size': page_size,
                'total_pages': total_pages,
                'total_items': user_data_count,
                'has_next': has_next,


                'has_pervious': has_pervious}

        return JsonResponse(data,safe=False)
    except Exception as exe:
        res = {'error': exe}
        return JsonResponse(res, safe=False)
@api_view(['GET','POST'])
def book_create(request):
    try:
        data=json.loads(request.body)
        if 'id' in data:
            book_id = data.pop('id')
            book_update=Book.objects.filter(id=book_id).update(**data)
            if book_update:
                book_data = Book.objects.get(id=book_id)
                book_serlizer_data=book_serlizer(book_data).data
                return JsonResponse(book_serlizer_data,safe=False)
            else:
                return JsonResponse("Updation Failed")
        else:
            book_create = Book.objects.create(**data)
            if book_create:
                book_serlizer_data = book_serlizer(book_create).data
                return JsonResponse(book_serlizer_data, safe=False)
            else:
                return JsonResponse("Creation Failed")
    except Exception as exe:
        res = {'error': exe}
        return JsonResponse(json.dumps(res), safe=False)

@api_view(['DELETE'])
def author_delete(request,author_id):
    author_delete=Author.objects.filter(id=author_id).delete()
    if author_delete:
        return JsonResponse("Deletred", safe=False)
    else:
        return JsonResponse("Deletion Failed", safe=False)
