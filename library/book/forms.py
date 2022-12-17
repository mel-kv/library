from datetime import date, timedelta

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.views.generic import UpdateView

from library.book.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        readonly_fields = ['title']
        fields = ['reader', 'date_checked_out', 'date_to_return', 'status']

    def clean(self):
        cleaned_data = super(BookForm, self).clean()

        date_checked_out = cleaned_data.get('date_checked_out')
        date_to_return = cleaned_data.get('date_to_return')
        reader = cleaned_data.get('reader')

        # Values may be None if the fields did not pass previous validations.
        if reader is not None:
            if date_to_return > date_checked_out + timedelta(days=20):
                self.add_error(None, ValidationError('Reader cannot take the book for more than 20 days'))

                return cleaned_data



