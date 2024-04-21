from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title(titleni tekshirish) if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavahsi harflardan iborat bo'lishi kerak"
                }
            )

        # check title and author from database exictanse(title va author bazada bo'lsa)
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                "status": False,
                "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklab bo'lamydi"
            })

        return data

    def validate_price(self, price):
        if price < 0 or price > 124000000:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx xato kiritilgan"
                }
            )
