from django_quickbooks import QUICKBOOKS_ENUMS, qbwc_settings
from django_quickbooks.objects.customer_pos import Customer
from django_quickbooks.processors.base import ResponseProcessor, ResponseProcessorMixin
from django_quickbooks.signals import qb_object_created, qb_object_queried, qb_object_updated

LocalCustomer = qbwc_settings.LOCAL_MODEL_CLASSES['Customer']


class CustomerQueryResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_CUSTOMER_POS
    op_type = QUICKBOOKS_ENUMS.OPP_QR
    local_model_class = LocalCustomer
    obj_class = Customer

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for customer_ret in list(self._response_body):
            customer = self.obj_class.from_lxml(customer_ret)
            qb_object_queried.send(self.obj_class, instance=customer, realm=realm)
        return True


class CustomerAddResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_CUSTOMER_POS
    op_type = QUICKBOOKS_ENUMS.OPP_ADD
    local_model_class = LocalCustomer
    obj_class = Customer

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for customer_ret in list(self._response_body):
            customer = self.obj_class.from_lxml(customer_ret)
            qb_object_created.send(self.obj_class, instance=customer, realm=realm)

        return True


class CustomerModResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_CUSTOMER_POS
    op_type = QUICKBOOKS_ENUMS.OPP_MOD
    local_model_class = LocalCustomer
    obj_class = Customer

    def process(self, realm):
        cont = super().process(realm)
        if not cont:
            return False
        for customer_ret in list(self._response_body):
            customer = self.obj_class.from_lxml(customer_ret)
            qb_object_updated.send(self.obj_class, instance=customer, realm=realm)
            return True
