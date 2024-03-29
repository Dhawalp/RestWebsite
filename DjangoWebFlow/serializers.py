from DjangoWebFlow.models import Book
from rest_framework import serializers

# ModelSerializer automatically creates serializer class with its fields corresponding to model fields.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('url', 'name', 'isbn', 'publisher', 'publisher_year', 'date_created', 'date_modified', 'owner')
