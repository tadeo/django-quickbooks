from django.utils.module_loading import import_string

from django_quickbooks.exceptions import QBObjectNotImplemented

ALTERNATIVES = {
    'ItemService': ('Item',),
}


def import_object_cls(resource_name):
    for class_name, alternatives in ALTERNATIVES.items():
        if resource_name in alternatives:
            resource_name = class_name

    try:
        return import_string('%s.%s' % (__package__, resource_name))
    except ImportError:
        raise QBObjectNotImplemented(f"Object {resource_name} is not found")


from django_quickbooks.objects.customer import \
    Customer

from django_quickbooks.objects.address import \
    BillAddress, \
    ShipAddress

from django_quickbooks.objects.invoice import \
    ItemService, \
    InvoiceLine, \
    Invoice

from django_quickbooks.objects.customer_pos import \
    Customer as CustomerPOS

from django_quickbooks.objects.item_inventory_pos import \
    ItemInventory

from django_quickbooks.objects.department_pos import \
    Department

from django_quickbooks.objects.purchase_order_pos import \
    PurchaseOrder, \
    PurchaseOrderItem

from django_quickbooks.objects.voucher_pos import \
    Voucher, \
    VoucherItem

from django_quickbooks.objects.vendor_pos import \
    Vendor
