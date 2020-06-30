from django_quickbooks import QUICKBOOKS_ENUMS
from django_quickbooks.services.base import Service
from django_quickbooks.utils import get_xml_meta_info, xml_setter


class SalesReceiptPOSService(Service):
    add_fields = ['SalesReceiptItem',
                  'TenderAccount',
                  'TenderCash',
                  'TenderCreditCard',
                  'TenderDeposit',
                  'TenderGift']
    complex_fields = ['BillingInformation',
                      'ShippingInformation']
    qb_type = None

    def add(self, object):
        return self._add(QUICKBOOKS_ENUMS.RESOURCE_SALES_RECEIPT_POS, object)

    def update(self, object):
        return self._update(QUICKBOOKS_ENUMS.RESOURCE_SALES_RECEIPT_POS, object)

    def all(self):
        self._all(QUICKBOOKS_ENUMS.RESOURCE_SALES_RECEIPT_POS)

    def find_by_id(self, id):
        return self._find_by_id(QUICKBOOKS_ENUMS.RESOURCE_SALES_RECEIPT_POS, id)
