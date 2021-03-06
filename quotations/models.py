from django.db.models.fields         import BooleanField, DecimalField
from django.db.models.deletion       import CASCADE
from django.db.models.fields.related import ForeignKey

from core.models import TimeStampModel

class Quotation(TimeStampModel):
    application  = ForeignKey('applications.Application', on_delete=CASCADE)
    price        = DecimalField(max_digits=10, decimal_places=2, null=True)
    is_completed = BooleanField(null=True, default=False)
    master       = ForeignKey('masters.Master', on_delete=CASCADE, related_name='hired_master')

    class Meta:
        db_table = 'quotations'
