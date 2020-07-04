from django_quickbooks import QUICKBOOKS_ENUMS, qbwc_settings
from django_quickbooks.objects.vendor_pos import Vendor
from django_quickbooks.processors.base import ResponseProcessor, ResponseProcessorMixin
from django_quickbooks.signals import qb_object_created, qb_object_queried

LocalVendor = qbwc_settings.LOCAL_MODEL_CLASSES['VendorPOS']


class VendorQueryResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_VENDOR_POS
    op_type = QUICKBOOKS_ENUMS.OPP_QR
    local_model_class = LocalVendor
    obj_class = Vendor

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for vendor_ret in list(self._response_body):
            vendor = self.obj_class.from_lxml(vendor_ret)
            qb_object_queried.send(self.obj_class, instance=vendor, realm=realm)

        return True


class VendorAddResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_VENDOR_POS
    op_type = QUICKBOOKS_ENUMS.OPP_ADD
    local_model_class = LocalVendor
    obj_class = Vendor

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for vendor_ret in list(self._response_body):
            vendor = self.obj_class.from_lxml(vendor_ret)
            if vendor.CompanyName:
                local_vendor = self.find_by_name(vendor.CompanyName, field_name='company_name')

                if local_vendor:
                    self.update(local_vendor, vendor)
                    qb_object_created.send(local_vendor.__class__, instance=local_vendor)
        return True
