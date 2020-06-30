from django_quickbooks import QUICKBOOKS_ENUMS, qbwc_settings
from django_quickbooks.objects.voucher_pos import Voucher
from django_quickbooks.processors.base import ResponseProcessor, ResponseProcessorMixin
from django_quickbooks.signals import qb_object_created
from django.utils import timezone

LocalVoucher = qbwc_settings.LOCAL_MODEL_CLASSES['VoucherPOS']


class VoucherQueryResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_VOUCHER_POS
    op_type = QUICKBOOKS_ENUMS.OPP_QR
    local_model_class = LocalVoucher
    obj_class = Voucher

    def process(self, realm):
        # fixme should handle duplicate response in someway
        cont = super().process(realm)
        if not cont:
            return False
        for voucher_ret in list(self._response_body):
            voucher = self.obj_class.from_lxml(voucher_ret)
            local_voucher = None
            if voucher.ListID:
                local_voucher = self.find_by_list_id(voucher.ListID)
            elif not local_voucher and voucher.Name:
                local_voucher = self.find_by_name(voucher.Name)

            if local_voucher:
                self.update(local_voucher, voucher)
            # else:
            #     self.create(voucher)
        return True


class VoucherAddResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_VOUCHER_POS
    op_type = QUICKBOOKS_ENUMS.OPP_ADD
    local_model_class = LocalVoucher
    obj_class = Voucher

    def process(self, realm):
        # fixme should handle duplicate error response in someway
        cont = super().process(realm)
        if not cont:
            return False
        for voucher_ret in list(self._response_body):
            voucher = self.obj_class.from_lxml(voucher_ret)
            if voucher.InvoiceNumber:
                local_voucher = self.find_by_name(voucher.InvoiceNumber, field_name='id')

                if local_voucher:
                    local_voucher.qbd_object_id = voucher.ListID
                    local_voucher.qbd_object_updated_at = timezone.now()
                    local_voucher.save()
                    # self.update(local_voucher, voucher)
                    qb_object_created.send(local_voucher.__class__, instance=local_voucher, realm=realm)
        return True
