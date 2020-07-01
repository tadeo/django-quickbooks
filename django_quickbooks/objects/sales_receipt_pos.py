from django_quickbooks.objects.base import BaseObject
from django_quickbooks.validators import SchemeValidator
from django_quickbooks.objects import AddressPOS


class SalesReceiptItem(BaseObject):
    fields = dict(Qty=dict(validator=dict(type=SchemeValidator.INTTYPE)),
                  Price=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
                  ListID=dict(validator=dict(type=SchemeValidator.IDTYPE)),
                  )


class TenderAccount(BaseObject):
    fields = dict(
        TenderAmount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
    )


class TenderCash(BaseObject):
    fields = dict(
        TenderAmount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
    )


class TenderCreditCard(BaseObject):
    fields = dict(
        CardName=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        TenderAmount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
    )


class TenderDeposit(BaseObject):
    fields = dict(
        TenderAmount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
    )


class TenderGift(BaseObject):
    fields = dict(
        GiftCertificateNumber=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        TenderAmount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
    )


class ShippingInformation(AddressPOS):
    pass


class BillingInformation(AddressPOS):
    pass


class SalesReceipt(BaseObject):
    fields = dict(
        Comments=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=300)),
        PriceLevelNumber=dict(validator=dict(type=SchemeValidator.INTTYPE)),
        # SalesReceiptType may have one of the following values: Sales,Return,Deposit,Refund,Payout,Payin
        SalesReceiptType=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=40)),
        ShipDate=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        TxnID=dict(validator=dict(type=SchemeValidator.IDTYPE)),
        TxnDate=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        SalesReceiptItem=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
        TenderAccount=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
        TenderCash=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
        TenderCreditCard=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
        TenderDeposit=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
        TenderGift=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
        CustomerListID=dict(validator=dict(type=SchemeValidator.IDTYPE)),
        Discount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        DiscountPercent=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        # HistoryDocStatus may have one of the following values: Regular
        HistoryDocStatus=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        ItemsCount=dict(validator=dict(type=SchemeValidator.INTTYPE)),  # read-only
        QuickBooksFlag=dict(validator=dict(type=SchemeValidator.BOOLTYPE)),
        SalesReceiptNumber=dict(validator=dict(type=SchemeValidator.STRTYPE)),  # read-only
        # StoreExchangeStatus may have one of the following values: Modified
        StoreExchangeStatus=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        StoreNumber=dict(validator=dict(type=SchemeValidator.INTTYPE)),
        Subtotal=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        Total=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        TaxAmount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        # TaxCategory may have one of the following values: Exempt
        TaxCategory=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        TaxPercentage=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        TenderType=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        # choose Workstation to ensure your cash drawer transaction integrity
        Workstation=dict(validator=dict(type=SchemeValidator.INTTYPE)),
        BillingInformation=dict(validator=dict(type=SchemeValidator.OBJTYPE)),  # read-only
        ShippingInformation=dict(validator=dict(type=SchemeValidator.OBJTYPE)),  # read-only
        PromoCode=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        IncludeRetElement=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
    )

    @staticmethod
    def get_service():
        from django_quickbooks.services.sales_receipt_pos import SalesReceiptPOSService
        return SalesReceiptPOSService
