from django_quickbooks.objects.base import BaseObject
from django_quickbooks.validators import SchemeValidator


class Vendor(BaseObject):
    fields = dict(
        City=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=31)),
        CompanyName=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=40)),  # unique
        EMail=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=99)),
        FirstName=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=30)),
        IsInactive=dict(validator=dict(type=SchemeValidator.BOOLTYPE)),
        LastName=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=30)),
        Notes=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=254)),
        Phone=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=21)),
        Phone2=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=21)),
        PostalCode=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=13)),
        Salutation=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=15)),
        State=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=21)),
        Street=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=41)),
        VendorCode=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=3)),
        ListID=dict(validator=dict(type=SchemeValidator.IDTYPE)),
    )

    @staticmethod
    def get_service():
        from django_quickbooks.services.vendor_pos import VendorPOSService
        return VendorPOSService
