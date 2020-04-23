from django_quickbooks.objects.base import BaseObject
from django_quickbooks.validators import SchemeValidator


class PurchaseOrderItem(BaseObject):
    fields = dict(
        ListID=dict(required=True, validator=dict(type=SchemeValidator.IDTYPE)),
        Qty=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
    )


class PurchaseOrder(BaseObject):
    fields = dict(
        Associate=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=40)),
        CancelDate=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        TxnID=dict(validator=dict(type=SchemeValidator.IDTYPE)),
        CompanyName=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        Discount=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        DiscountPercent=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        Fee=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        Instructions=dict(validator=dict(type=SchemeValidator.STRTYPE, max_length=2000)),
        ItemsCount=dict(validator=dict(type=SchemeValidator.INTTYPE)),
        PurchaseOrderNumber=dict(validator=dict(type=SchemeValidator.INTTYPE)),
        # PurchaseOrderStatusDesc may have one of the following values: Open, Pending, Closed, Suggested
        PurchaseOrderStatusDesc=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        QtyDue=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        QtyOrdered=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        QtyReceived=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        StartShipDate=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        # StoreExchangeStatus may have one of the following values: Modified
        StoreExchangeStatus=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        StoreNumber=dict(validator=dict(type=SchemeValidator.INTTYPE)),
        Subtotal=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        Total=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        TxnDate=dict(validator=dict(type=SchemeValidator.STRTYPE)),
        UnfilledPercent=dict(validator=dict(type=SchemeValidator.FLOATTYPE)),
        VendorListID=dict(required=True, validator=dict(type=SchemeValidator.INTTYPE)),
        PurchaseOrderItem=dict(many=True, validator=dict(type=SchemeValidator.OBJTYPE)),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def get_service():
        from django_quickbooks.services.purchase_order import PurchaseOrderService
        return PurchaseOrderService
