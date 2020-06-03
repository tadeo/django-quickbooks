from django_quickbooks.objects.base import BaseObject
from django_quickbooks.validators import SchemeValidator


class Customer(BaseObject):
    fields = dict(
        ListID=dict(validator=dict(type=SchemeValidator.IDTYPE)),
        CompanyName=dict(validator=dict(type=SchemeValidator.STRTYPE)),

        # CustomerDiscType may have one of the following values: None,PriceLevel,Percentage
        CustomerDiscType=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        EMail=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        FirstName=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        LastName=dict(required=True, validator=dict(type=SchemeValidator.STRTYPE)),
        Phone=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        Notes=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        Phone2=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        # PriceLevelNumber may have one of the following values: 1,2,3,4
        PriceLevelNumber=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        Salutation=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        BillAddress=dict(validator=dict(type=SchemeValidator.OBJTYPE)),
        ShipAddress=dict(validator=dict(type=SchemeValidator.OBJTYPE)),

        AccountBalance=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),  # read-only
        AccountLimit=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),  # read-only
        IsAcceptingChecks=dict(validator=dict(type=SchemeValidator.BOOLTYPE)),
        CustomerDiscPercent=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        IsUsingWithQB=dict(validator=dict(type=SchemeValidator.BOOLTYPE)),
        StoreExchangeStatus=dict(validator=dict(type=SchemeValidator.STRTYPE)),  # read-only
        IsUsingChargeAccount=dict(validator=dict(type=SchemeValidator.BOOLTYPE)),
    )

    @staticmethod
    def get_service():
        from django_quickbooks.services.customer_pos import CustomerPOSService
        return CustomerPOSService
