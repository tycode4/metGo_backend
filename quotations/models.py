from django.db.models.fields         import DecimalField
from django.db.models.deletion       import CASCADE
from django.db.models.fields.related import ForeignKey

from core.models import TimeStampModel

class Quotation(TimeStampModel):
    application_master = ForeignKey('applications.ApplicationMaster', on_delete=CASCADE)
    price              = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'quotations'