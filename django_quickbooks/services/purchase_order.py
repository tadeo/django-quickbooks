from django_quickbooks import QUICKBOOKS_ENUMS
from django_quickbooks.services.base import Service


class PurchaseOrderService(Service):
    qb_type = None

    def add(self, object):
        return self._add(QUICKBOOKS_ENUMS.RESOURCE_PURCHASE_ORDER, object)

    def update(self, object):
        return self._update(QUICKBOOKS_ENUMS.RESOURCE_PURCHASE_ORDER, object)

    def all(self):
        return self._all(QUICKBOOKS_ENUMS.RESOURCE_PURCHASE_ORDER)

    def find_by_id(self, id):
        return self._find_by_id(QUICKBOOKS_ENUMS.RESOURCE_PURCHASE_ORDER, id)
