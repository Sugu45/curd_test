from rest_framework import serializers
from .models import *
class author_serlizer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class book_serlizer(serializers.ModelSerializer):
    author=author_serlizer(read_only=True)
    class Meta:
        model=Book
        fields='__all__'




