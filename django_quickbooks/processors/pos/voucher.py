from django_quickbooks import QUICKBOOKS_ENUMS, qbwc_settings
from django_quickbooks.objects.voucher_pos import Voucher
from django_quickbooks.processors.base import ResponseProcessor, ResponseProcessorMixin
from django_quickbooks.signals import qb_object_created, qb_object_queried

LocalVoucher = qbwc_settings.LOCAL_MODEL_CLASSES['VoucherPOS']


class VoucherQueryResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_VOUCHER_POS
    op_type = QUICKBOOKS_ENUMS.OPP_QR
    local_model_class = LocalVoucher
    obj_class = Voucher

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for voucher_ret in list(self._response_body):
            voucher = self.obj_class.from_lxml(voucher_ret)
            qb_object_queried.send(self.obj_class, instance=voucher, realm=realm)

        return True


class VoucherAddResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_VOUCHER_POS
    op_type = QUICKBOOKS_ENUMS.OPP_ADD
    local_model_class = LocalVoucher
    obj_class = Voucher

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for voucher_ret in list(self._response_body):
            voucher = self.obj_class.from_lxml(voucher_ret)
            qb_object_created.send(self.obj_class, instance=voucher, realm=realm)

        return True
