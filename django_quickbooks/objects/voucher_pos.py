from django_quickbooks.objects.base import BaseObject
from django_quickbooks.validators import SchemeValidator


class VoucherItem(BaseObject):
    fields = dict(
        ListID=dict(required=True, validator=dict(type=SchemeValidator.IDTYPE)),
        QtyReceived=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
    )


class Voucher(BaseObject):
    fields = dict(
        Associate=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=40)),
        Comments=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=300)),
        TxnID=dict(validator=dict(type=SchemeValidator.IDTYPE)),
        # CompanyName=dict(validator=dict(type=SchemeValidator.STRTYPE)),  # response only
        Discount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        DiscountPercent=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        Fee=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        Freight=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        # ItemsCount=dict(validator=dict(type=SchemeValidator.INTTYPE)),  # response only
        # QuickBooksFlag may have one of the following values: NotPosted,Completed,Error,UnbilledPurchases
        QuickBooksFlag=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        # StoreExchangeStatus may have one of the following values: Modified
        StoreExchangeStatus=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        StoreNumber=dict(validator=dict(type=SchemeValidator.INTTYPE)),
        Subtotal=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        Total=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        TxnDate=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        VendorListID=dict(required=True, validator=dict(type=SchemeValidator.IDTYPE)),
        VoucherNumber=dict(validator=dict(type=SchemeValidator.INTTYPE)),
        # VoucherType may have one of the following values: Receiving,Return
        VoucherType=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        VoucherItem=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
        PurchaseOrderTxnID=dict(validator=dict(type=SchemeValidator.IDTYPE)),
        InvoiceDate=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        InvoiceNumber=dict(validator=dict(type=SchemeValidator.INTTYPE)),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def get_service():
        from django_quickbooks.services.voucher import VoucherService
        return VoucherService
