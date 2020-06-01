from django_quickbooks import QUICKBOOKS_ENUMS
from django_quickbooks.services.base import Service


class CustomerPOSService(Service):
    complex_fields = ['BillAddress', 'ShipAddress']

    qb_type = None

    def add(self, object):
        return self._add(QUICKBOOKS_ENUMS.RESOURCE_CUSTOMER_POS, object)

    def update(self, object):
        return self._update(QUICKBOOKS_ENUMS.RESOURCE_CUSTOMER_POS, object)

    def all(self):
        return self._all(QUICKBOOKS_ENUMS.RESOURCE_CUSTOMER_POS)

    def find_by_id(self, id):
        return self._find_by_id(QUICKBOOKS_ENUMS.RESOURCE_CUSTOMER_POS, id)

    def find_by_full_name(self, full_name):
        return self._find_by_full_name(QUICKBOOKS_ENUMS.RESOURCE_CUSTOMER_POS, full_name)
