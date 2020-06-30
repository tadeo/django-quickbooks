from django_quickbooks.processors.base import \
    ResponseProcessor

from django_quickbooks.processors.customer import \
    CustomerQueryResponseProcessor, \
    CustomerAddResponseProcessor, \
    CustomerModResponseProcessor

from django_quickbooks.processors.invoice import \
    InvoiceQueryResponseProcessor, \
    InvoiceAddResponseProcessor, \
    InvoiceModResponseProcessor

from django_quickbooks.processors.item_service import \
    ItemServiceQueryResponseProcessor

from django_quickbooks.processors.pos.item_inventory import \
    ItemInventoryQueryResponseProcessor, \
    ItemInventoryAddResponseProcessor

from django_quickbooks.processors.pos.voucher import \
    VoucherQueryResponseProcessor, \
    VoucherAddResponseProcessor

from django_quickbooks.processors.pos.vendor import \
    VendorQueryResponseProcessor, \
    VendorAddResponseProcessor

from django_quickbooks.processors.pos.customer import \
    CustomerQueryResponseProcessor as CustomerQueryResponseProcessorPOS, \
    CustomerAddResponseProcessor as CustomerAddResponseProcessorPOS, \
    CustomerModResponseProcessor as CustomerModResponseProcessorPOS

from django_quickbooks.processors.pos.sales_receipt import \
    SalesReceiptQueryResponseProcessor, \
    SalesReceiptAddResponseProcessor
