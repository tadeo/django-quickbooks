from django_quickbooks.objects.base import BaseObject
from django_quickbooks.validators import SchemeValidator


class Address(BaseObject):
    fields = dict(
        City=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        PostalCode=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        State=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        Street=dict(validator=dict(type=SchemeValidator.STRTYPE)),
    )

