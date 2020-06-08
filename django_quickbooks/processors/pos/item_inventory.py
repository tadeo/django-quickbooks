from django_quickbooks import QUICKBOOKS_ENUMS, qbwc_settings
from django_quickbooks.objects.item_inventory_pos import ItemInventory
from django_quickbooks.processors.base import ResponseProcessor, ResponseProcessorMixin
from django_quickbooks.signals import qb_object_created, qb_object_queried
from django.utils import timezone

LocalItemInventory = qbwc_settings.LOCAL_MODEL_CLASSES['ItemInventory']


class ItemInventoryQueryResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_ITEM_INVENTORY_POS
    op_type = QUICKBOOKS_ENUMS.OPP_QR
    local_model_class = LocalItemInventory
    obj_class = ItemInventory

    def process(self, realm):
        # fixme should handle duplicate response in someway
        cont = super().process(realm)
        if not cont:
            return False
        for item_ret in list(self._response_body):
            item = self.obj_class.from_lxml(item_ret)
            if item.ALU:
                local_item = self.find_by_name(item.ALU, field_name='id')

                if local_item:
                    local_item.qbd_object_id = item.ListID
                    local_item.qbd_object_updated_at = timezone.now()
                    local_item.save()
                    # self.update(local_item, item)
                    qb_object_queried.send(self.obj_class, instance=local_item, realm=realm)
            # else:
            #     self.create(item_inventory)
        return True


class ItemInventoryAddResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_ITEM_INVENTORY_POS
    op_type = QUICKBOOKS_ENUMS.OPP_ADD
    local_model_class = LocalItemInventory
    obj_class = ItemInventory

    def process(self, realm):
        # fixme should handle duplicate error response in someway
        cont = super().process(realm)
        if not cont:
            return False
        for item_ret in list(self._response_body):
            item = self.obj_class.from_lxml(item_ret)
            if item.ALU:
                local_item = self.find_by_name(item.ALU, field_name='id')

                if local_item:
                    local_item.qbd_object_id = item.ListID
                    local_item.qbd_object_updated_at = timezone.now()
                    local_item.save()
                    # self.update(local_item, item)
                    qb_object_created.send(self.obj_class, instance=local_item, realm=realm)
        return True
