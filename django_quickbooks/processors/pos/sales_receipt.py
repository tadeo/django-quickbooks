from django_quickbooks import QUICKBOOKS_ENUMS, qbwc_settings
from django_quickbooks.objects.sales_receipt_pos import SalesReceipt
from django_quickbooks.processors.base import ResponseProcessor, ResponseProcessorMixin
from django_quickbooks.signals import qb_object_created, qb_object_queried, qb_object_updated

LocalReceipt = qbwc_settings.LOCAL_MODEL_CLASSES['SalesReceiptPOS']


class SalesReceiptQueryResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_SALES_RECEIPT_POS
    op_type = QUICKBOOKS_ENUMS.OPP_QR
    local_model_class = LocalReceipt
    obj_class = SalesReceipt

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for receipt_ret in list(self._response_body):
            receipt = self.obj_class.from_lxml(receipt_ret)
            qb_object_queried.send(self.obj_class, instance=receipt, realm=realm)

        return True


class SalesReceiptAddResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_SALES_RECEIPT_POS
    op_type = QUICKBOOKS_ENUMS.OPP_ADD
    local_model_class = LocalReceipt
    obj_class = SalesReceipt

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for receipt_ret in list(self._response_body):
            receipt = self.obj_class.from_lxml(receipt_ret)
            qb_object_created.send(self.obj_class, instance=receipt, realm=realm)

        return True
