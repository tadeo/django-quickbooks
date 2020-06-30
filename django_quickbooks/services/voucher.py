from django_quickbooks import QUICKBOOKS_ENUMS
from django_quickbooks.services.base import Service


class VoucherService(Service):
    """
    Vouchers are added and queried using the SDK requests VoucherAdd and VoucherQuery.
    They cannot be modified or deleted either in the QBPOS UI or via the SDK: this preserves
    the integrity of the transaction history
    """
    add_fields = ['VoucherItem']
    qb_type = None

    def add(self, object):
        return self._add(QUICKBOOKS_ENUMS.RESOURCE_VOUCHER_POS, object)

    def all(self):
        return self._all(QUICKBOOKS_ENUMS.RESOURCE_VOUCHER_POS)

    def find_by_id(self, id):
        return self._find_by_id(QUICKBOOKS_ENUMS.RESOURCE_VOUCHER_POS, id)
